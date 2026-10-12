---
name: mandala-book-studio
description: Erstelle, übersetze oder überarbeite Mandala-Malbücher mit konsistenten Charakteren, passenden Covervorschauen und KDP-Druckprüfung. Nutze die enthaltene Giggle-Dumplings-Vorlage für neue Themen und Figuren; nicht für beliebige Dokumente oder einzelne unabhängige Illustrationen.
---

# Mandala-Buchstudio

Erstelle nachvollziehbar zusammengesetzte Buchfassungen aus echten Einzelbildern. Unterstützt neue Bücher aus der Vorlage, Lokalisierung und gezielte Korrekturen. Die Vorlage ist eine Arbeitsgrundlage, keine bestätigte KDP-Freigabe.

## Einstieg und Quellen

- Wähle die vom Nutzer gemeinte neueste Fassung. Produktionsordner, Downloads, PNGs und Interior-PDF können verschiedene Motive enthalten. Das tatsächlich ausgewählte Interior hat bei Abweichungen Vorrang; extrahiere bei Bedarf dessen eingebettete Bilder.
- Verwende bevorzugt die mitgelieferten Assets; keine ursprünglichen Rechnerpfade voraussetzen. Das Manifest assets/template/book-de.json erklärt Reihenfolge, Seitenrollen und Wiederverwendung. book-en.json verwendet dieselben textfreien Motive und originale englische Einleitungs-/Mitmachseiten.
- Arbeite in einer neuen Ausgabe, nicht in den Vorlagenassets. Speichere Änderungen und ihre Quellen im neuen Manifest. Übernimm die Giggle-Dumplings-Marke nur, wenn das neue Buch weiterhin zu dieser Reihe gehören soll.
- Eine Skill-Anwendung autorisiert weder Veröffentlichung noch Änderungen am KDP-Konto.

## Modus wählen

- Neues Thema oder andere Charaktere: Lies references/neues-buch.md; starte mit der Seiten- und Figurenplanung.
- Übersetzung, Schrift, Bildänderungen: Lies references/gestaltung.md. Nutze die verfügbare Imagegen-Skill für Rasterbearbeitung und die PDF-Skill für Druckdateien.
- KDP-Datei, Beschnittmeldung, Druckprüfung: Lies references/kdp.md und verifiziere die aktuellen offiziellen Regeln für die gewählte Ausstattung.
- Details zur vorhandenen Fassung und Quellen: references/vorlage.md. Lade nur die für den aktuellen Auftrag relevanten Referenzen.

## Gestaltung, die hier entscheidend ist

1. Schrift gehört zur Illustration: lebendige Konturbuchstaben, passende Strichstärke, großzügige Lesbarkeit. Untertitel folgen der Krümmung ihres Bands. Weiße Rechtecke oder aufgesetzte Standardtextflächen über Bildschrift waren in diesem Projekt ausdrücklich unerwünscht.
2. Motivnamen wie „Hasen-Mandala“ sind für diese Vorlage entbehrlich. Entferne bei neuen Fassungen Namen, Beschriftungsrahmen und nur dazugehörige Ornamente sauber; bewahre Zeichnung und natürliche untere Kontur. Namen in der Charaktervorstellung und notwendige Mitmachtexte bleiben.
3. Ein Bildeditor kann beim Entfernen oder Verschieben Hintergrund und Konturen ergänzen; kontrolliere das Ergebnis. Eine angeforderte Verschiebung um 45 Pixel wurde einmal etwa doppelt so groß umgesetzt. Tatsächliche Position und Druckabstände prüfen, nicht die Promptzahl als Beweis behandeln.
4. Rückseitenvorschauen müssen aus der fertigen Ausgabe stammen. Vier passende Kategorien: Tiere, Charaktere, klassisches Mandala, Mitmachseite. Originalbilder direkt im Layout einsetzen, proportional skalieren und bei Bedarf als Ausschnitt beschneiden. Bildgeneration darf hier keine ähnlichen Ersatzmotive erfinden.
5. Änderungen an Rastercover und deterministischer Buchsatz sind getrennte Aufgaben. Bewege Aufkleber mit natürlicher Hintergrundrekonstruktion; platziere echte Vorschaubilder danach aus den gespeicherten Interior-Assets.
6. Bei Übersetzung dieses Reihenbuchs bleiben „Giggle Dumplings“ und „Giggle Home“ unverändert. Prüfe Titel, Impressum, Charaktertexte, Aktivitäten, Bildunterschriften, Ausgabenbadge und Coverrückseite; verwende natürliches Deutsch statt Wort-für-Wort-Übertragung.

## Erstellung und Abschluss

- Manifest als verbindliche Inhaltsliste führen. Keine fiktiven Labyrinthe, Unterschiede-Suchen oder Aufgaben in Beschreibung, Cover oder Shopvorschau ankündigen.
- Bild für Bild bearbeiten; typische Figuren zunächst in einer Referenzübersicht festlegen. Keine Sammelgrafik als Ersatz für getrennte Buchseiten.
- Textfreie wiederverwendete Seiten pixelgleich übernehmen. Bei Figuren-/Textbearbeitung Identität, Linienqualität und Aufgabeninhalt visuell kontrollieren.
- Für die enthaltene 70-Seiten-Architektur kann scripts/build_interior.py ein angepasstes Manifest setzen. Es bearbeitet keine Bilder. Neue Seitenzahlen, Bleed-Modi oder Seitentypen erfordern eine passend geänderte Planung.
- scripts/audit_print_files.py liefert Maße, Seitenzahl und tatsächliche Rasterauflösung sowie optional gerenderte Coverrandprüfungen. Warnungen nicht als Freigabe wegformulieren: das Skript ersetzt weder Sichtprüfung noch KDP-Previewer.
- Ganze PDFs rendern und alle Seiten ansehen, nicht nur die ersten Seiten. Details von Textseiten, Cover, beschnittkritischen Aufklebern und Suchaufgaben zusätzlich groß prüfen. Drucklinien nur auf QA-Ansichten, niemals im Upload-PDF.
- Getrennte Cover- und Interior-PDFs, optional Einzelbilder-ZIP sowie klare aktuelle Versionsnamen liefern. Bei reiner Coverkorrektur das unveränderte Interior nicht neu exportieren.
- Druckeignung, bestandene lokale Prüfung und tatsächliche KDP-Freigabe unterscheiden. Konkrete Restprobleme nennen. Einen Proof/Probeabzug empfehlen, wenn Veröffentlichung als nächster Schritt ansteht.
