import os
import tkinter as tk
from tkinter import scrolledtext, Frame
import threading
from model_utils import initialize_model, generate_code_suggestion
from gui_utils import create_gui, start_typing_timer, set_root
from code_execution import execute_code, reset_output, set_output_text, set_text_area, set_root_in_code_execution

# Pfad zum Skriptverzeichnis
script_dir = os.path.dirname(os.path.abspath(__file__))
local_model_path = os.path.join(script_dir, "codegen-350M-mono")

# Globale Variablen für Tokenizer, Modell und Timer
tokenizer = None
model = None
typing_delay = 500  # in Millisekunden
typing_timer = None
model_loaded = False  # Flag, um den Ladezustand des Modells zu verfolgen

# GUI-Erstellung und Konfiguration der Benutzeroberfläche
root = tk.Tk()
root.title("Code Editor")

# Setzen der root Variable im gui_utils Modul
set_root(root)

# Setzen der root Variable im code_execution Modul
set_root_in_code_execution(root)

# Textfeld für die Code-Eingabe
text_area, suggestion_label, execute_button, reset_button, output_text = create_gui(root)

# Setzen der Variablen im code_execution Modul
set_output_text(output_text)
set_text_area(text_area)

# Start des Modell-Ladevorgangs
load_thread = threading.Thread(target=initialize_model, args=(script_dir, local_model_path, suggestion_label, root))
load_thread.daemon = True
load_thread.start()

# Start der Haupt-Event-Schleife
root.mainloop()
