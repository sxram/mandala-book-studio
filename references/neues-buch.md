# Neues Buch aus der Vorlage

## Seiten übernehmen oder ersetzen

Die Auswahl ist eine Ausgangsplanung, keine Verpflichtung, stets 33 Motive oder fünf Figuren zu verwenden.

| Seitenrolle | Motive der Vorlage | Sinnvolle Behandlung |
| --- | --- | --- |
| Klassische Mandalas | 03, 06, 10, 13, 18, 21, 25, 28, 31 | Neun textfreie Motive können unverändert bleiben, wenn Thema und Schwierigkeitsgrad passen. |
| Tiermandalas | 01, 04, 07, 11, 14, 17, 20, 23, 27, 30 | Zehn Motive können unverändert bleiben oder gezielt zum Thema ersetzt werden. |
| Charaktermandalas | 02, 05, 09, 12, 15, 19, 22, 26, 29, 32 | Zehn Motive mit den neuen Figuren bearbeiten; auch Mehrfigurenbilder und Accessoires kontrollieren. |
| Mitmachseiten | 08, 16, 24, 33 | Drei Suchbilder und eine freie Zeichenseite: Figuren ändern, Aufgaben prüfen, benötigten Text lokalisieren. |
| Einleitung | Titel, Impressum, Charaktervorstellung | Neuer Buchtitel, passende Ausgabe, neue Figuren und aktuelle Angaben. |
| Cover | Rückseite, Rücken, Vorderseite | Neue Figuren/Texte; echte finale Vorschauen; Maße aus neuer Ausstattung berechnen. |

Eine Variante mit neun klassischen und zehn Tiermotiven unverändert benötigt typischerweise 14 bearbeitete Motivseiten plus Einleitung und Cover. Wenn alle 19 übernommenen Seiten zum Thema passen, spart das Arbeit ohne die Serienqualität zu verändern.

## Konkreter Arbeitsablauf

1. Neue Ausgabe im Arbeitsverzeichnis anlegen. book-de.json oder book-en.json kopieren. Alle dortigen relativen Assetpfade relativ zum jeweiligen Manifest auflösen; beim Kopieren Pfade entsprechend neu setzen oder benötigte Assets mitkopieren. Vorlagenassets nicht überschreiben.
2. Namen/Thema/Sprache/Alter aus dem Auftrag übernehmen. Wenn Figuren noch nicht beschrieben sind, einen passenden Vorschlag und eine Referenzübersicht entwickeln. Keine Veröffentlichung oder neue Charakteranzahl ohne Auftrag voraussetzen.
3. Für jedes Motiv status=reuse, replace oder edit im neuen Manifest setzen. Grund und Ziel festhalten. Manifest darf zusätzliche Felder enthalten; der Satzhelper nutzt hauptsächlich asset-Pfade und Layout.
4. Neue Figurenreferenz erstellen, Identitätsmerkmale fixieren, dann charakterhaltige Motive einzeln bearbeiten. Originalkomposition als Ausgangspunkt benutzen; nicht jedes Motiv neu erfinden, wenn nur Charakterwechsel gewünscht ist.
5. Einleitungsseiten, Titel und Impressum anpassen. Alte Reihenmarke nur behalten, wenn die neue Ausgabe dazugehört. Insbesondere Giggle Home nicht automatisch als Herausgebermarke einer fremden Reihe übernehmen.
6. Wiederverwendete und neue Bilder zusammenstellen. In der gewählten Reihenfolge prüfen: Inhalt, Textreste, Figuren, Linien und Suchbildlösungen.
7. Interior setzen. Beispiel-Aufruf: python scripts/build_interior.py /absoluter/pfad/neue-ausgabe/book.json /absoluter/pfad/neue-ausgabe/Interior.pdf. Laufzeit mit reportlab verwenden; ggf. verfügbare Workspace-Abhängigkeiten laden.
8. Erst nach finaler Seitenzahl Covergröße berechnen. Cover in nativer Grafikqualität planen, neue Titel/Badges/Charaktere integrieren. Vier Originalausschnitte aus genau diesem neuen Interior als Rückseitenvorschau einsetzen.
9. Druckprüfung nach kdp.md, sichtbare Gesamtprüfung, dann getrennte Dateien liefern. Titel/Beschreibung/Tags aus dem tatsächlichen Manifest ableiten; Inhalt und Kategorien müssen übereinstimmen.

## Satzarchitektur der Vorlage

Titelseite (1), Impressum (2), Charaktervorstellung (3), Leerseite (4). Danach jedes Motiv auf einer Vorderseite mit leerer Rückseite. Für N Motive ergibt das 4 + 2N Seiten; bei N=33 sind es 70. Motiv n beginnt auf PDF-Seite 5 + 2(n-1).

Das ist für einseitige Ausmalmotive gedacht. Es ist kein allgemeiner KDP-Zwang, und KDP prüft übermäßig viele Leerseiten. Die Absicht im Manuskript/Produkt klar halten und tatsächlichen Previewer prüfen. Für A4/Etsy keine KDP-Rückenmaße übernehmen; separate Druck-/Downloadversion planen.

## Beispiel zum Aufrufen der Skill

„Nutze $mandala-book-studio. Erstelle eine neue deutsche Ausgabe mit fünf Waldwesen statt der Giggle Dumplings. Behalte die neun klassischen Mandalas und passende Tiermandalas bei. Ersetze die Figuren auf allen zehn Charaktermandalas und vier Mitmachseiten. Passe Einleitung und Cover an, verwende echte Vorschauen und liefere getrennte PDFs plus Einzelbilder-ZIP.“
