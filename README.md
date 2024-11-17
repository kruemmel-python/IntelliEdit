# AI CodeHelper

AI CodeHelper ist ein benutzerfreundlicher Code-Editor mit integrierter KI-gestützter Code-Vorschlagsfunktion. Er bietet Syntaxhervorhebung, Zeilennummern und die Möglichkeit, Code direkt im Editor auszuführen. Code-Vorschlagsfunktion durch Tastenkombination STRG + SPACE


![image](https://github.com/user-attachments/assets/a44a5fe0-c36f-418a-a666-8933281f14dc)


## Inhaltsverzeichnis

- [Installation](#installation)
- [Funktionen](#funktionen)
- [Verwendung](#verwendung)
- [Beiträge](#beiträge)
- [Lizenz](#lizenz)

## Installation

1. **Klonen des Repositories**:
   ```sh
   git clone https://github.com/kruemmel-python/IntelliEdit.git
   cd IntelliEdit
   ```

2. **Installieren der Abhängigkeiten**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Starten des Editors**:
   ```sh
   python main.py
   ```

## Funktionen

- **Syntaxhervorhebung**: Unterstützung für Python-Syntaxhervorhebung.
- **Zeilennummern**: Anzeige von Zeilennummern neben dem Code.
- **Code-Vorschläge**: KI-gestützte Code-Vorschläge basierend auf dem eingegebenen Text. STRG + SPACE
- **Code-Ausführung**: Direkte Ausführung des Codes im Editor mit Anzeige der Ausgabe und Fehlermeldungen.

## Verwendung

1. **Starten des Editors**:
   ```sh
   python main.py
   ```

2. **Code eingeben**:
   - Geben Sie Ihren Python-Code in das Haupt-Textfeld ein.
   - Zeilennummern werden automatisch neben dem Code angezeigt.
   - Der Code wird farblich hervorgehoben, um die Lesbarkeit zu verbessern.

3. **Code-Vorschläge erhalten**:
   - Drücken Sie `Ctrl + Space`, um KI-gestützte Code-Vorschläge basierend auf dem eingegebenen Text zu erhalten.
   - Die Vorschläge werden im Vorschlagsfeld angezeigt.

4. **Code ausführen**:
   - Klicken Sie auf die Schaltfläche "Code ausführen", um den eingegebenen Code auszuführen.
   - Die Ausgabe und Fehlermeldungen werden im Ausgabefeld angezeigt.

5. **Ausgabe zurücksetzen**:
   - Klicken Sie auf die Schaltfläche "Ausgabe zurücksetzen", um das Ausgabefeld zu leeren.

## Beiträge

Beiträge sind herzlich willkommen! Wenn Sie einen Fehler gefunden haben oder eine neue Funktion vorschlagen möchten, erstellen Sie bitte ein Issue oder einen Pull Request.

1. **Forken des Repositories**:
   ```sh
   git clone https://github.com//kruemmel-python/IntelliEdit.git
   cd IntelliEdit
   git checkout -b feature/IhreFunktion
   ```

2. **Installieren der Abhängigkeiten**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Änderungen vornehmen**:
   - Fügen Sie Ihre Änderungen hinzu und testen Sie sie gründlich.

4. **Commit und Push**:
   ```sh
   git add .
   git commit -m "Beschreibung Ihrer Änderungen"
   git push origin feature/IhreFunktion
   ```

5. **Pull Request erstellen**:
   - Erstellen Sie einen Pull Request auf GitHub und beschreiben Sie Ihre Änderungen.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der [LICENSE](LICENSE)-Datei.

## Kontakt

Wenn Sie Fragen haben oder Unterstützung benötigen, können Sie mich über [Ihre E-Mail-Adresse](mailto:IhreE-Mail-Adresse) kontaktieren.

## Danksagungen

- [Pygments](https://pygments.org/) für die Syntaxhervorhebung.
- [Transformers](https://huggingface.co/transformers/) für die KI-gestützten Code-Vorschläge.

---

Vielen Dank, dass Sie AI CodeHelper verwenden!
```

### `requirements.txt`

Stellen Sie sicher, dass Sie eine `requirements.txt`-Datei im Projektverzeichnis haben, die alle erforderlichen Abhängigkeiten auflistet:

```
transformers
pygments
```

### `LICENSE`
```
MIT License

Copyright (c) 2023 Ralf Krümmel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
