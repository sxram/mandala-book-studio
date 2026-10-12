# KDP: Beschnitt, sichere Flächen und Druckqualität

Offizielle Quellen, geprüft am 12.10.2026; bei einem neuen Druckauftrag aktuelle Angaben erneut prüfen:
- [Taschenbuchcover erstellen](https://kdp.amazon.com/en_US/help/topic/G201953020)
- [Richtlinien zum Einreichen](https://kdp.amazon.com/en_US/help/topic/G201857950)
- [Coverrechner und Vorlage](https://kdp.amazon.com/cover-calculator)

## Der nachgewiesene Fehler dieser Produktion

KDP beanstandete bei der englischen Ausgabe fehlenden Beschnitt auf Vorder- und Rückseite. Die Datei war bereits 1253,35 x 810 pt groß, aber das Bild nur 1215 x 810 pt mit einem Versatz von 19,17504 pt. Links und rechts entstanden jeweils etwa 6,76 mm weiße Streifen. Richtige PDF-Abmessungen beweisen daher noch keinen ausgefüllten Beschnitt.

Die damalige Reparatur verbreiterte die eingefügte Grafik um etwa 3,16 Prozent horizontal, sodass sie die vorhandene Seite füllte. Kein zusätzlicher weißer Rand und keine zweite Beschnittzugabe. Dies war eine konkrete Reparatur einer bereits gestalteten Datei; neue Bücher besser unmittelbar auf dem korrekten Gesamtformat anlegen statt pauschal Figuren zu strecken.

Danach waren beide rechten Frontbadges zu randnah. Sie wurden einzeln nach innen versetzt. Der untere Badge wurde anschließend tiefer gesetzt, geriet durch Bildgeneration zunächst zu nah an den unteren Rand und musste erneut korrigiert werden. Jede endgültige Position an Trim- UND Sicherheitslinie prüfen. Nur innerhalb der Trimlinie zu liegen reicht für wichtige Schrift nicht.

## Geometrie

KDP-Cover: eine zusammenhängende PDF-Seite mit Rückseite, Rücken, Vorderseite. Beschnitt rundum 0,125 Zoll. Der Hintergrund füllt die gesamte äußere PDF-Fläche. Maße und Rücken aus endgültiger Seitenzahl, Papier und Druckart bestimmen; Vorlage/Calculator bevorzugen.

Für Schwarz-Weiß auf weißem Papier gilt im geprüften KDP-Stand Rücken = Seitenzahl x 0,002252 Zoll. Gesamtbreite = 2 x Buchbreite + Rücken + 0,25 Zoll. Gesamthöhe = Buchhöhe + 0,25 Zoll.

Vorlage: 70 Seiten, 8,5 x 11 Zoll, Rücken 0,15764 Zoll, Cover 17,40764 x 11,25 Zoll bzw. 1253,35008 x 810 pt. 1 pt = 1/72 Zoll. Das Innenbuch hat ohne Interior-Bleed 612 x 792 pt. Bei anderer Seitenzahl/Papierwahl neu rechnen. Bei dieser 70-Seiten-Vorlage kein Rückentext.

Als robuste Layoutreserve wichtige Texte/Badges mindestens 0,25 Zoll vom äußeren PDF-Rand anordnen; konkrete sichere Bereiche der KDP-Vorlage haben Vorrang. Ganze Aufkleber einschließlich Umrandung sichtbar halten und keinen Titel verdecken. Barcodebereich gemäß aktueller Vorlage reservieren; eine bisher nicht beanstandete fehlende Reservierung ist kein Beweis für Eignung.

## Auflösung: offener Qualitätsmangel der alten Vorlage

KDP nennt mindestens 300 dpi für Coverbilder. Prüfe Pixelzahl bei tatsächlicher Druckgröße, nicht nur DPI-Metadaten oder Exportauflösung. Unsere 1536 x 1024 px große Spread-Grafik erreicht bei etwa 17,41 x 11,25 Zoll nur ungefähr 88 x 91 dpi. Ein 300-dpi-PNG-Export aus diesem Bild fügt keine echten Details hinzu. Cover dieser Vorlage sind deshalb Layout-/Gestaltungsreferenzen, keine zertifizierten Druckmaster.

Für das konkrete 70-Seiten-Cover werden bei 300 dpi etwa 5223 x 3375 Pixel benötigt. Generierung, Quelldateien oder fachgerecht geprüftes Upscaling entsprechend planen; wenn ein Werkzeug das nicht nativ liefert, die Grenze klar nennen. Auch bei Ausmalseiten tatsächliche Auflösung und Strichqualität prüfen. Keine Freigabe behaupten, solange relevante Warnungen bestehen.

## Weitere Druckprüfungen

- Einbettung von Fonts, Transparenzen und Farbräumen prüfen; aktuelle CMYK-Empfehlung der KDP-Coverhilfe beachten. Keine unkontrollierte pauschale Farbraumkonvertierung, die Linien oder Farben verschlechtert.
- Kein Passwortschutz, keine Schnittmarken, Kontrolllinien, Vorlagentexte oder Druckhilfen in den Upload-Dateien. Hochauflösende Bilder nicht unnötig mehrfach komprimieren.
- Titel, Sprache, Ausgabe, Namen und ggf. ISBN müssen mit den gewählten Buchdaten übereinstimmen. Artwork-Hintergrund darf in den Beschnitt, wichtige Texte nicht.
- Interior hat eigene Rand-/Bleed-Vorgaben. Kein Coverbeschnitt auf jede Malbuchseite anwenden. Innenrand nach Seitenzahl/Gutter prüfen, alle Seiten gleich groß, keine abgeschnittenen Motive.
- Cover komplett und zusätzlich mit Trim-/Sicherheitslinien auf einer separaten QA-Kopie ansehen. Randstreifen auf weißes Papier prüfen. Badgepositionen nach Rendern messen.
- Suchbildzahlen und Vorschauen gehören ebenfalls zur Qualitätsprüfung, auch wenn KDP sie nicht ausdrücklich beanstandet hat.
- Lokal bestandene Prüfungen ersetzen nicht den KDP-Previewer oder die finale Prüfung. Keine automatische Upload-/Veröffentlichungsberechtigung aus diesem Workflow ableiten.

## Helfer

python scripts/audit_print_files.py Interior.pdf Cover.pdf --paper white --trim-width 8.5 --trim-height 11 --render-cover --report pruefung.json

Das Audit prüft Seite/Geometrie, tatsächliche dpi direkt platzierter Rasterbilder und optional gerenderte weiße Außenränder. Es prüft keine Textabstände, Barcodepositionen, Suchlösungen oder KDP-Account-Einstellungen. Es zeichnet keine Hilfslinien in das Upload-PDF. Für abweichende Ausstattung keine passende Größe erraten: Manifest und aktuelle Vorlage aktualisieren.
