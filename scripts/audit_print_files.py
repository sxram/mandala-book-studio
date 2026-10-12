#!/usr/bin/env python3
"""Read-only print audit: geometry, effective raster dpi, optional cover edge analysis."""
import argparse
import json
import math
import shutil
import subprocess
import tempfile
from pathlib import Path
from pypdf import PdfReader
from pypdf.generic import ContentStream


def multiply(a, b):
    aa, ab, ac, ad, ae, af = a
    ba, bb, bc, bd, be, bf = b
    return (aa*ba+ac*bb, ab*ba+ad*bb, aa*bc+ac*bd, ab*bc+ad*bd,
            aa*be+ac*bf+ae, ab*be+ad*bf+af)


def image_placements(reader, page):
    found = []
    def walk(stream, resources, initial=(1, 0, 0, 1, 0, 0), depth=0):
        if stream is None or depth > 12:
            return
        matrix, stack = initial, []
        for operands, operator in ContentStream(stream, reader).operations:
            if operator == b'q':
                stack.append(matrix)
            elif operator == b'Q':
                matrix = stack.pop() if stack else initial
            elif operator == b'cm':
                matrix = multiply(matrix, tuple(float(x) for x in operands))
            elif operator == b'Do':
                objects = resources.get('/XObject', {})
                if hasattr(objects, 'get_object'):
                    objects = objects.get_object()
                obj = objects.get(operands[0])
                if obj is None:
                    continue
                obj = obj.get_object()
                if obj.get('/Subtype') == '/Image':
                    placed_w = math.hypot(matrix[0], matrix[1])
                    placed_h = math.hypot(matrix[2], matrix[3])
                    if placed_w and placed_h:
                        found.append({'pixels': [int(obj['/Width']), int(obj['/Height'])],
                                      'placed_points': [round(placed_w, 3), round(placed_h, 3)],
                                      'dpi': [round(float(obj['/Width']) * 72 / placed_w, 1),
                                              round(float(obj['/Height']) * 72 / placed_h, 1)]})
                elif obj.get('/Subtype') == '/Form':
                    form_matrix = tuple(float(x) for x in obj.get('/Matrix', (1, 0, 0, 1, 0, 0)))
                    form_resources = obj.get('/Resources', resources)
                    if hasattr(form_resources, 'get_object'):
                        form_resources = form_resources.get_object()
                    walk(obj, form_resources, multiply(matrix, form_matrix), depth + 1)
    resources = page['/Resources'].get_object()
    walk(page.get_contents(), resources)
    return found


def audit(interior, cover, trim_width=8.5, trim_height=11, paper='white', render_cover=False):
    interior, cover = Path(interior).resolve(), Path(cover).resolve()
    ir, cr = PdfReader(interior), PdfReader(cover)
    factor = {'white': 0.002252, 'cream': 0.0025}[paper]
    count = len(ir.pages)
    expected_cover = [(2 * trim_width + count * factor + .25) * 72,
                      (trim_height + .25) * 72]
    report = {'interior': str(interior), 'cover': str(cover), 'pages': count,
              'equipment_basis': {'trim_inches': [trim_width, trim_height],
                                  'ink': 'black-and-white', 'paper': paper},
              'expected_cover_points': expected_cover, 'errors': [], 'warnings': [],
              'checks_not_covered': ['safe text/badge positions', 'barcode area', 'color validation',
                                     'font embedding', 'activity solutions', 'KDP account settings',
                                     'final KDP approval']}
    if ir.is_encrypted or cr.is_encrypted:
        report['errors'].append('Encrypted PDF')
    for index, page in enumerate(ir.pages, 1):
        if abs(float(page.mediabox.width) - trim_width * 72) > .1 or abs(float(page.mediabox.height) - trim_height * 72) > .1:
            report['errors'].append(f'Interior page {index}: dimensions differ from no-bleed trim size')
    if len(cr.pages) != 1:
        report['errors'].append('Cover must have one full-spread page')
    if cr.pages:
        cp = cr.pages[0]
        report['actual_cover_points'] = [float(cp.mediabox.width), float(cp.mediabox.height)]
        if any(abs(a-b) > .1 for a, b in zip(report['actual_cover_points'], expected_cover)):
            report['errors'].append('Cover dimensions do not match final page count/paper/trim/bleed')
    for label, reader in [('interior', ir), ('cover', cr)]:
        images = []
        for index, page in enumerate(reader.pages, 1):
            for image in image_placements(reader, page):
                image['page'] = index
                images.append(image)
        report[label + '_raster_images'] = images
        if not images:
            report['warnings'].append(f'{label}: no measurable raster images found; may be vector content')
        low = [i for i in images if min(i['dpi']) < 299]
        if low:
            report['warnings'].append(f'{label}: {len(low)} placed raster image(s) below 300 dpi')
    if render_cover and cr.pages:
        renderer = shutil.which('pdftoppm')
        if not renderer:
            report['warnings'].append('pdftoppm unavailable: rendered edge check skipped')
        else:
            from PIL import Image
            with tempfile.TemporaryDirectory(prefix='mandala-audit-') as tmp:
                prefix = str(Path(tmp) / 'cover')
                subprocess.run([renderer, '-r', '72', '-png', '-singlefile', str(cover), prefix], check=True, capture_output=True)
                with Image.open(prefix + '.png') as opened:
                    image = opened.convert('RGB')
                w, h = image.size
                edges = {'left': (0, 0, 2, h), 'right': (w-2, 0, w, h),
                         'top': (0, 0, w, 2), 'bottom': (0, h-2, w, h)}
                stats = {}
                for name, box in edges.items():
                    cropped = image.crop(box)
                    pixels = list(cropped.get_flattened_data() if hasattr(cropped, 'get_flattened_data') else cropped.getdata())
                    ratio = sum(min(pixel) > 248 for pixel in pixels) / len(pixels)
                    stats[name] = round(ratio, 4)
                    if ratio > .95:
                        report['warnings'].append(f'Cover {name} edge nearly all white: inspect for missing bleed; white design can be intentional')
                report['cover_outer_edge_white_fraction'] = stats
    report['local_geometry_pass'] = not report['errors']
    report['kdp_approval'] = 'not established'
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('interior')
    parser.add_argument('cover')
    parser.add_argument('--trim-width', type=float, default=8.5)
    parser.add_argument('--trim-height', type=float, default=11)
    parser.add_argument('--paper', choices=['white', 'cream'], default='white')
    parser.add_argument('--render-cover', action='store_true')
    parser.add_argument('--report')
    args = parser.parse_args()
    result = audit(args.interior, args.cover, args.trim_width, args.trim_height, args.paper, args.render_cover)
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(text, encoding='utf8')
    print(text)
    raise SystemExit(2 if result['errors'] else 0)
