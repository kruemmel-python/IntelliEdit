
# IntelliEdit

**IntelliEdit** ist ein interaktiver Code-Editor mit integrierter Unterstützung für KI-basierte Codevorschläge. Es nutzt ein vortrainiertes Modell von Hugging Face, um während der Eingabe Codevorschläge zu generieren. Der Editor ermöglicht außerdem die direkte Ausführung und Ausgabe von Code innerhalb der Anwendung.

![image](https://github.com/user-attachments/assets/55f2ae52-6241-41aa-b1dc-e55f6fa1fc4f)



## Funktionen

- **KI-gestützte Codevorschläge**: IntelliEdit verwendet das Modell `Salesforce/codegen-350M-mono`, um basierend auf der Benutzereingabe intelligente Codevorschläge zu machen.
- **Interaktive GUI**: Eine benutzerfreundliche Oberfläche mit einem Editor, Vorschlagsfeld und Ausgabebereich.
- **Codeausführung**: Direkte Ausführung des eingegebenen Codes mit Ausgabe und Fehleranzeige.
- **Echtzeit-Vorschläge**: Automatische Vorschläge während der Eingabe mit einer kurzen Verzögerung, um die Benutzererfahrung zu verbessern.

## Installation

1. **Repository klonen:**
   ```bash
   git clone https://github.com/kruemmel-python/IntelliEdit/IntelliEdit.git
   cd IntelliEdit
   ```

2. **Abhängigkeiten installieren:**
   Stelle sicher, dass Python 3.8 oder neuer installiert ist. Installiere die benötigten Pakete:
   ```bash
   pip install -r requirements.txt
   ```

3. **Hugging Face-Modell herunterladen:**
   IntelliEdit lädt das Modell `Salesforce/codegen-350M-mono` beim ersten Start automatisch herunter.

## Verwendung

1. **Starten der Anwendung:**
   ```bash
   python IntelliEdit.py
   ```

2. **Funktionen der GUI:**
   - Schreibe deinen Code in das Haupttextfeld.
   - Während der Eingabe werden Vorschläge im unteren Bereich angezeigt.
   - Klicke auf **"Code ausführen"**, um deinen Code direkt im Editor auszuführen.
   - Die Ausgabe oder Fehlermeldungen erscheinen im Ausgabefeld.

3. **Vorschläge:** 
   IntelliEdit generiert KI-basierte Vorschläge basierend auf deiner Eingabe. Du kannst diese nutzen, um deinen Code effizient zu schreiben.

## Projektstruktur

```
IntelliEdit/
├── IntelliEdit.py       # Hauptskript für die Anwendung
├── README.md            # Diese Dokumentation
├── requirements.txt     # Abhängigkeiten
└── codegen-350M-mono/   # Lokale Kopie des Hugging Face-Modells (wird automatisch erstellt)
```

## Anforderungen

- **Python 3.8+**
- **Abhängigkeiten**:
  - `transformers`
  - `torch`
  - `tkinter`

Installiere die Abhängigkeiten mit:
```bash
pip install transformers torch
```

## Bekannte Probleme

- Das Modell benötigt Speicherplatz und Rechenleistung. Für langsamere Systeme wird empfohlen, kleinere Modelle oder alternative Hardwarebeschleunigung zu verwenden.
- Bei Netzwerkproblemen kann das Modell nicht automatisch heruntergeladen werden. In diesem Fall lade das Modell manuell von [Hugging Face](https://huggingface.co/Salesforce/codegen-350M-mono) herunter und speichere es im Verzeichnis `codegen-350M-mono`.

## Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**. Siehe die Datei `LICENSE` für weitere Details.

---

## Vorschläge und Verbesserungen

Beiträge sind willkommen! Erstelle ein Issue oder sende einen Pull-Request, um neue Ideen, Fehlerbehebungen oder Funktionen vorzuschlagen.
```

### Ergänzende Hinweise

  ```
  transformers
  torch
  ```

