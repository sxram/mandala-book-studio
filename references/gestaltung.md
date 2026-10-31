# Schrift, Figuren und Bildbearbeitung

## Aus dieser Produktion gelernt

Die erste deutsche Ausgabe war gestalterisch nicht brauchbar: Gerade Computerschrift lag mit weißen Masken über Originalschrift. Das zerstörte geschwungene Bänder und wirkte retuschiert. Der Nutzer verlangte integrierte Bildschrift. Titelseite, Cover, Charaktervorstellung und Aktivitäten wurden anschließend mit Bildbearbeitung lokalisiert.

Aufgaben-/Titelschrift darf groß sein: runde lebendige Konturbuchstaben mit weißer Füllung und schwarzen Außenlinien passen zum ausmalbaren Stil. Fließtext auf der Charakterseite braucht ruhigere, gut lesbare Buchstaben und passende Zeilenumbrüche. Impressum darf schlicht bleiben; keine Angaben erfinden. Rechtliche Pflichtangaben gesondert prüfen, wenn ein rechtssicheres Impressum beauftragt ist.

## Lokalisierungs-Prompt als Ausgangspunkt

Use case: text-localization.
Edit target: [Originalseite].
Replace ONLY [konkret bezeichnete Textbereiche] with exact text: [vollständiger Wortlaut].
Match original playful rounded hand lettering and line weights. Subtitle follows the existing ribbon arc, including rotated letters along its curve.
Preserve original characters, frame, ornaments, composition and aspect ratio.
No pasted label, flat computer-font overlay, white rectangle or visible retouching.
Output complete edited page.

Immer die tatsächlichen Texte und Invarianten einsetzen. Namen, Zahlen, Umlaute, Interpunktion und Lesbarkeit nach dem Rendern prüfen. Lange Wörter können breitere Bänder, eine andere Zeilenaufteilung oder kürzere natürliche Formulierungen erfordern.

## Motivnamen entfernen

Use case: precise-object-edit.
Remove the bottom motif caption, its capsule frame and flourishes belonging solely to that label. Preserve the entire main drawing and finish touched lower outlines naturally. Leave a clean page margin. No replacement text, panel, crop or unrelated additions.

Nicht einfach die letzte Bildzeile abschneiden: Pfoten, Blätter und Rahmen können verbunden sein. Prüfe jeden unteren Motivrand. Bestehende Motive ohne Caption müssen nicht neu generiert werden.

## Charakterwechsel

Bei fünf Figuren Namen, Silhouette, Gesicht, typische Accessoires und Größenverhältnisse in einer Referenzübersicht festhalten. Beispiel: Kappe, Schleife, Kochhut, Brille, Schlafmütze waren Identitätsmerkmale der Giggle Dumplings. Für eine neue Reihe dürfen andere Merkmale gewählt werden; alte Merkmale nicht unbeabsichtigt mit übernehmen.

Use case: precise-object-edit oder compositing.
Replace ONLY [alte Figur und Accessoires] with [neue Figur anhand Referenz]. Keep pose/position, supporting mandala structure and page framing. White background, closed crisp black outlines, no gray shading, no new text. Remove all remaining old-brand character details.

Bei Mehrfigurenbildern alle alten Figuren gezielt ersetzen. Tiermandalas bleiben nur dann unverändert, wenn sie keine alten Figuren oder themenspezifischen Symbole enthalten. Bildgeneration kann Geometrie verändern: Formen, Gesicht, Gliedmaßen, geschlossene Ausmalflächen und Wiedererkennbarkeit kontrollieren.

## Mitmachaufgaben

Die Vorlage hat drei Suchbilder und eine Zeichenseite. Bei Suchbildern jede Zielmarkierung zählen und auf einer separaten Lösungsansicht markieren; diese muss nicht mit veröffentlicht werden. Zahl in der Überschrift mit dem tatsächlichen Bild abgleichen. Gleichartige dekorative Sterne/Herzen dürfen nicht zu mehreren plausiblen Lösungen führen. Diese Zählprüfung wurde in der bisherigen Produktion nicht als vollständiger Nachweis dokumentiert und ist bei einem neuen Buch nachzuholen.

Die Zeichenseite benötigt echte freie Bereiche und darf durch den Figurenwechsel nicht vollständig ausgefüllt werden. Keine unbekannten Rätselarten im Verkaufstext behaupten.

## Cover und echte Vorschauen

Die vier ursprünglichen Rückseitenbilder waren erfundene Beispiele. Später wurden Originalausschnitte aus den Motiven 01 (Fuchs), 26 (fünf Freunde), 03 (Lotus), 33 (eigener Dumpling) direkt im PDF eingebettet. Das neue Buch benötigt eigene echte Beispiele aus seinem finalen Manifest. Nicht englische Seiten als Vorschau einer deutschen Ausgabe verwenden, sofern sichtbare Texte betroffen sind.

Bildrahmen und bestehende Beschriftung bewahren. Innerhalb der Rahmen proportional skalieren und bei Bedarf die Originalbilder beschneiden; Konturen nicht nachzeichnen lassen. Ausschnitte müssen die Kategorien erkennbar zeigen, dürfen aber als Ausschnitte statt vollständiger Seiten gestaltet sein.

Aufkleber sind komplette Objekte einschließlich weißer Außenkante, Herzform und Schmuck. Verschieben ist nicht dasselbe wie globales Zoomen. „English Edition“-Herz: genügend Abstand oben/rechts, ohne Titelüberdeckung. „33 magical mandalas“-Badge: rechts/unten innerhalb der sicheren Fläche, ohne Figurengesicht zu verdecken. Nach jeder Änderung beide Positionen, Schrift und Hintergrund erneut prüfen.


## Graue Flächen auf weißem Papier

Beim Neuaufbau der Giggle-Dumplings-Ausgabe am 31.10.2026 wurden vorhandene Rasterbilder unverändert in ein anderes PDF-Format gesetzt. Dadurch blieben helle graue Hintergrundrechtecke und Schattierungen aus den Quellen erhalten. Korrekte Seitenmaße und unveränderte Bilddaten waren kein Nachweis für einen reinweißen Malbuchhintergrund. Die frühere, abgelaufene Chatdatei mit „CLEAN_WHITE_SMOOTH_LINES“ im Namen konnte nicht aus der bloßen Formatkonvertierung wiederhergestellt werden.

Wenn ein reinweißer Hintergrund gewünscht ist, vor dem finalen Satz jede tatsächlich verwendete Innenseite prüfen: Außenrand außerhalb des Bildes mit freien Flächen innerhalb des Bildes vergleichen und auf graue Rechtecke, Verläufe und Schattierungen achten. In einer separaten QA-Ansicht Kontrast verstärken oder Helligkeitswerte messen, damit sehr helle Flächen erkennbar werden. Keine Prüfkontrastverstärkung in die Druckdatei übernehmen.

Ungewollte Grauflächen gezielt in neuen Arbeitskopien bereinigen. Keine pauschale harte Schwarzweiß-Schwelle ohne Prüfung: Sie kann dünne Linien, kleine Schrift, i-Punkte und weiche Linienkanten beschädigen. Dunkle gewollte Konturen und geschlossene Ausmalflächen erhalten; beabsichtigte Flächen von Fehlern unterscheiden. Vorher-/Nachherdetails prüfen, insbesondere Charaktertexte, Suchbildsymbole und dicht gezeichnete Mandalas. Textfreie Motive dürfen für eine ausdrücklich beauftragte Hintergrundbereinigung angepasst werden; die sonstige Vorgabe der pixelgleichen Wiederverwendung ist dann kein Grund, den Fehler beizubehalten.

Verfahren, Parameter und betroffene Seiten im Ausgabemanifest festhalten und die fertigen PDFs erneut vollständig rendern. Deutsche und englische Ausgabe jeweils prüfen, auch wenn sie Motive teilen. „Clean white“, „glatte Linien“ oder „bereinigt“ nur behaupten, wenn die konkrete Ausgabe tatsächlich so bearbeitet und visuell geprüft wurde. Bleibt eine graue Fläche bestehen, sie als offenen Mangel nennen und die Ausgabe nicht als bereinigt ausgeben.
