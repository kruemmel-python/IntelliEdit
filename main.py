"""
Code-Editor-Anwendung

Dieses Modul enthält die Hauptlogik einer Code-Editor-Anwendung mit einer grafischen Benutzeroberfläche,
die von `tkinter` bereitgestellt wird. Es bietet Funktionen zum Schreiben, Ausführen und
Zurücksetzen von Code sowie zur Integration eines KI-Modells zur Code-Vervollständigung.

Module:
-------
- gui_utils: Enthält Funktionen zur Erstellung und Verwaltung der Benutzeroberfläche.
- code_execution: Beinhaltet die Logik zur Codeausführung und -anzeige.
- model_utils: Initialisiert das KI-Modell und generiert Code-Vorschläge.

Globale Variablen:
------------------
- script_dir (str): Der Verzeichnispfad des Skripts.
- local_model_path (str): Der Speicherpfad für das lokale Modell.
- tokenizer: Der Tokenizer für das KI-Modell.
- model: Das geladene KI-Modell.
- typing_delay (int): Verzögerung in Millisekunden zwischen Tastatureingaben.
- typing_timer: Timer-Objekt zur Steuerung der Eingabeverzögerung.
- model_loaded (bool): Gibt an, ob das KI-Modell erfolgreich geladen wurde.
"""

import os
import tkinter as tk
from tkinter import scrolledtext, Frame
import threading
from model_utils import initialize_model, generate_code_suggestion
from gui_utils import create_gui, start_typing_timer, set_root
from code_execution import (
    execute_code,
    reset_output,
    set_output_text,
    set_text_area,
    set_root_in_code_execution,
)

# Pfad zum Skriptverzeichnis
script_dir = os.path.dirname(os.path.abspath(__file__))
local_model_path = os.path.join(script_dir, "codegen-350M-mono")

# Globale Variablen für Tokenizer, Modell und Timer
tokenizer = None
model = None
typing_delay = 500  # in Millisekunden
typing_timer = None
model_loaded = False  # Flag, um den Ladezustand des Modells zu verfolgen

def main() -> None:
    """
    Hauptfunktion zum Starten der Anwendung.

    Diese Funktion initialisiert die grafische Benutzeroberfläche, lädt das Modell
    für Codevorschläge und startet die Haupt-Event-Schleife der Anwendung.

    Ablauf:
    -------
    1. Erstellen des Hauptfensters (`root`) mit `tkinter`.
    2. Konfiguration der GUI-Elemente, einschließlich Textfelder und Buttons.
    3. Initialisierung des Modells in einem separaten Thread.
    4. Start der Haupt-Event-Schleife mit `root.mainloop()`.

    Verwendete Funktionen:
    -----------------------
    - set_root(root): Konfiguriert die `root`-Variable im `gui_utils`-Modul.
    - set_root_in_code_execution(root): Konfiguriert die `root`-Variable im `code_execution`-Modul.
    - create_gui(root): Erstellt die GUI und gibt GUI-Elemente zurück.
    - initialize_model(script_dir, local_model_path, suggestion_label, root):
      Lädt das KI-Modell in einem separaten Thread.

    Hinweise:
    ---------
    - Das Modell wird in einem separaten Thread geladen, um die Haupt-Event-Schleife nicht zu blockieren.
    - `root` ist das Hauptfenster der Anwendung, das von `tkinter` verwaltet wird.
    """
    global root

    # GUI-Erstellung und Konfiguration der Benutzeroberfläche
    root = tk.Tk()
    root.title("Code Editor")

    # Setzen der root-Variable im gui_utils-Modul
    set_root(root)

    # Setzen der root-Variable im code_execution-Modul
    set_root_in_code_execution(root)

    # Textfeld für die Code-Eingabe
    text_area, suggestion_label, execute_button, reset_button, output_text = create_gui(
        root
    )

    # Setzen der Variablen im code_execution-Modul
    set_output_text(output_text)
    set_text_area(text_area)

    # Start des Modell-Ladevorgangs
    load_thread = threading.Thread(
        target=initialize_model, args=(script_dir, local_model_path, suggestion_label, root)
    )
    load_thread.daemon = True
    load_thread.start()

    # Start der Haupt-Event-Schleife
    root.mainloop()

if __name__ == "__main__":
    main()
