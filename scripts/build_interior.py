#!/usr/bin/env python3
"""Set a single-sided coloring-book interior from a relative-path manifest; no image edits."""
import argparse
import json
from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas


def build(manifest_path, output_path):
    manifest_path = Path(manifest_path).resolve()
    data = json.loads(manifest_path.read_text(encoding='utf8'))
    base = manifest_path.parent
    layout = data['layout']
    if layout.get('interior_bleed', False):
        raise ValueError('This helper supports no-bleed interiors only; plan a separate bleed layout')
    width, height = layout['trim_points']
    outside = layout['outside_margin_points']
    inside = layout['inside_margin_points']
    vertical = layout['vertical_margin_points']
    if min(width, height) <= 0 or min(outside, inside, vertical) < 0:
        raise ValueError('Invalid page geometry')
    if width <= outside + inside or height <= 2 * vertical:
        raise ValueError('Margins leave no image area')
    ordered = list(data['frontmatter'])
    for motif in data['motifs']:
        ordered.append(motif)
        if layout.get('blank_reverse', True):
            ordered.append(None)
    # Resolve all inputs before creating the destination.
    resolved = []
    for entry in ordered:
        if entry is None:
            resolved.append(None)
            continue
        img_path = (base / entry['asset']).resolve()
        if not img_path.is_file():
            raise FileNotFoundError(img_path)
        with Image.open(img_path) as im:
            image_size = im.size
        resolved.append((img_path, image_size))
    output_path = Path(output_path).resolve()
    if any(item and item[0] == output_path for item in resolved):
        raise ValueError('Output would overwrite an asset')
    if output_path.exists():
        raise FileExistsError('Choose a new output filename; existing PDF is preserved')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output_path), pagesize=(width, height), pageCompression=1)
    c.setTitle(data.get('title', 'Mandala coloring book'))
    c.setAuthor(data.get('author', ''))
    for number, item in enumerate(resolved, 1):
        if item:
            path, (iw, ih) = item
            left = inside if number % 2 else outside
            available_width = width - inside - outside
            available_height = height - 2 * vertical
            scale = min(available_width / iw, available_height / ih)
            draw_w, draw_h = iw * scale, ih * scale
            x = left + (available_width - draw_w) / 2
            y = (height - draw_h) / 2
            c.drawImage(str(path), x, y, width=draw_w, height=draw_h)
        c.showPage()
    c.save()
    return {'output': str(output_path), 'pages': len(resolved), 'motifs': len(data['motifs'])}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest')
    parser.add_argument('output')
    args = parser.parse_args()
    print(json.dumps(build(args.manifest, args.output), ensure_ascii=False, indent=2))
