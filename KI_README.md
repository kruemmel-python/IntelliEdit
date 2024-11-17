# AI CodeHelper - KI-Dokumentation

## Überblick

AI CodeHelper integriert eine KI-gestützte Code-Vorschlagsfunktion, die auf dem Modell `Salesforce/codegen-350M-mono` basiert. Dieses Modell ist speziell für die Generierung von Code-Vorschlägen trainiert und kann offline verwendet werden, nachdem es einmal heruntergeladen wurde.

## Verwendete KI

- **Modell**: `Salesforce/codegen-350M-mono`
- **Bibliothek**: `transformers` von Hugging Face
- **Funktion**: Generierung von Code-Vorschlägen basierend auf dem eingegebenen Text
- **Modellgröße**: Das Modell hat eine Größe von etwa 1.34 GB.

## Offline-Nutzung

AI CodeHelper kann vollständig offline verwendet werden, nachdem das Modell einmal heruntergeladen wurde. Dies ermöglicht eine schnelle und zuverlässige Nutzung ohne Internetverbindung.

### Schritte zur Offline-Nutzung

1. **Modell herunterladen**:
   - Beim ersten Start des Editors wird das Modell automatisch heruntergeladen und gespeichert.
   - Der Fortschritt des Downloads wird im Vorschlagsfeld angezeigt.

2. **Modell laden**:
   - Nach dem Herunterladen wird das Modell automatisch geladen und steht für die Generierung von Code-Vorschlägen zur Verfügung.
   - Das Modell wird im lokalen Verzeichnis gespeichert, sodass es bei zukünftigen Starts des Editors schnell geladen werden kann.

3. **Code-Vorschläge erhalten**:
   - Geben Sie Ihren Python-Code in das Haupt-Textfeld ein.
   - Drücken Sie `Ctrl + Space`, um KI-gestützte Code-Vorschläge basierend auf dem eingegebenen Text zu erhalten.
   - Die Vorschläge werden im Vorschlagsfeld angezeigt.

## Vorteile der Offline-Nutzung

- **Schnelligkeit**: Keine Verzögerungen durch Internetverbindungen.
- **Zuverlässigkeit**: Unabhängig von der Internetverfügbarkeit.
- **Datenschutz**: Ihre Daten bleiben lokal und werden nicht an externe Server gesendet.

## Technische Details

- **Modellgröße**: Das Modell `Salesforce/codegen-350M-mono` hat eine Größe von etwa 1.34 GB.
- **Speicherplatz**: Stellen Sie sicher, dass genügend Speicherplatz auf Ihrem Gerät verfügbar ist, um das Modell zu speichern.
- **Systemanforderungen**: Eine moderne CPU und mindestens 4 GB RAM werden empfohlen, um eine reibungslose Nutzung zu gewährleisten.

## Hinweise

- **Modellaktualisierungen**: Wenn eine neue Version des Modells verfügbar ist, können Sie das Modell manuell aktualisieren, indem Sie den entsprechenden Code in `model_utils.py` anpassen.
- **Fehlerbehebung**: Wenn Probleme beim Laden oder Verwenden des Modells auftreten, überprüfen Sie die Internetverbindung und stellen Sie sicher, dass genügend Speicherplatz verfügbar ist.

## Kontakt

Wenn Sie Fragen haben oder Unterstützung benötigen, können Sie mich über [ralf.kruemmel+python@outlook.de](mailto:ralf.kruemmel+python@outlook.de) kontaktieren.

---

Vielen Dank, dass Sie AI CodeHelper verwenden!
