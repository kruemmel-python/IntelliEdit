import os
import tkinter as tk
from tkinter import scrolledtext, Frame
from transformers import AutoTokenizer, AutoModelForCausalLM
import threading
import sys
import io
import sys
sys.path.insert(0, os.path.abspath('.')) 

# Pfad zum Skriptverzeichnis
script_dir = os.path.dirname(os.path.abspath(__file__))
local_model_path = os.path.join(script_dir, "codegen-350M-mono")

# Globale Variablen für Tokenizer, Modell und Timer
tokenizer = None
model = None
typing_delay = 500  # in Millisekunden
typing_timer = None
model_loaded = False  # Flag, um den Ladezustand des Modells zu verfolgen

def initialize_model():
    """Initialisiert das Modell und den Tokenizer in einem separaten Thread.

    Lädt das Modell und den Tokenizer aus dem Hugging Face-Modellhub.
    Setzt das Flag `model_loaded` auf True, wenn das Modell erfolgreich geladen wurde,
    und aktualisiert die Anzeige in der Benutzeroberfläche.

    Falls ein Fehler beim Laden des Modells auftritt, wird dies in der Konsole ausgegeben.
    """
    global tokenizer, model, model_loaded
    try:
        tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono", cache_dir=script_dir)
        tokenizer.pad_token = tokenizer.eos_token
        model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono", cache_dir=script_dir, ignore_mismatched_sizes=True)
        tokenizer.save_pretrained(local_model_path)
        model.save_pretrained(local_model_path)
        model_loaded = True
        root.after(0, lambda: suggestion_label.config(text="Modell geladen"))
    except Exception as e:
        print(f"Fehler beim Laden des Modells: {e}")
        model_loaded = False

def generate_code_suggestion(input_text):
    """Generiert Code-Vorschläge basierend auf dem eingegebenen Text.

    Die Generierung erfolgt in einem separaten Thread, um die Haupt-Thread-GUI
    nicht zu blockieren. Der generierte Code wird im Vorschlagsfeld der Benutzeroberfläche angezeigt.

    Args:
        input_text (str): Der vom Benutzer eingegebene Text, für den Code-Vorschläge generiert werden sollen.
    """
    if not model_loaded:
        root.after(0, lambda: suggestion_label.config(text="Modell wird geladen, bitte warten..."))
        return

    def background_task():
        try:
            input_ids = tokenizer.encode(input_text, return_tensors="pt")
            attention_mask = input_ids.ne(tokenizer.pad_token_id).float()
            output = model.generate(input_ids, attention_mask=attention_mask, max_new_tokens=30, num_return_sequences=1)
            generated_code = tokenizer.decode(output[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
        except Exception as e:
            generated_code = f"Fehler bei der Generierung: {str(e)}"
        root.after(0, lambda: suggestion_label.config(text=generated_code))

    threading.Thread(target=background_task).start()

def delayed_generate_code_suggestion():
    """Verzögert die Generierung der Code-Vorschläge.

    Holt den aktuellen Text aus dem Editor und übergibt ihn zur Code-Vorschlagsgenerierung.
    Diese Funktion wird verwendet, um die Anzahl der Generierungsanfragen zu steuern.
    """
    input_text = text_area.get("1.0", tk.END).strip()
    if input_text:
        generate_code_suggestion(input_text)

def start_typing_timer(event=None):
    """Startet einen Timer, um die Code-Vorschlagsgenerierung zu verzögern.

    Wird bei jeder Tastenfreigabe im Editor ausgelöst. Der Timer stellt sicher,
    dass die Vorschlagsgenerierung nur nach einer kurzen Pause ausgelöst wird.

    Args:
        event (tk.Event, optional): Das Tastaturereignis, das die Funktion auslöst.
    """
    global typing_timer
    if typing_timer is not None:
        root.after_cancel(typing_timer)
    typing_timer = root.after(typing_delay, delayed_generate_code_suggestion)

def execute_code():
    """Führt den Code aus, der im Editor geschrieben wurde.

    Die Funktion fängt die Ausgabe und Fehler ab und zeigt sie im Ausgabefeld an.
    """
    reset_output()
    code = text_area.get("1.0", tk.END).strip()
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()

    try:
        exec(code, {})
        output = sys.stdout.getvalue()
        error = sys.stderr.getvalue()
        if output:
            root.after(0, lambda: update_output_text(output))
        if error:
            root.after(0, lambda: update_output_text(error))
    except Exception as e:
        root.after(0, lambda: update_output_text(f"Fehler bei der Ausführung: {str(e)}\n"))
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

def update_output_text(text):
    """Aktualisiert das Ausgabefeld mit dem angegebenen Text.

    Args:
        text (str): Der anzuzeigende Text, typischerweise die Ausgabe oder Fehler bei der Ausführung.
    """
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, text)
    output_text.config(state=tk.DISABLED)

def reset_output():
    """Löscht den Inhalt des Ausgabefelds und setzt es in den schreibgeschützten Zustand zurück."""
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)

# GUI-Erstellung und Konfiguration der Benutzeroberfläche
root = tk.Tk()
root.title("Code Editor")

# Textfeld für die Code-Eingabe
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
text_area.pack(padx=10, pady=10)
text_area.bind("<KeyRelease>", start_typing_timer)

# Rahmen und Label für den Code-Vorschlag
suggestion_frame = Frame(root, bg="lightgrey", bd=2, relief="groove")
suggestion_frame.pack(fill="x", padx=10, pady=5)

suggestion_label = tk.Label(suggestion_frame, text="Lade Modell...", wraplength=700, justify="left", anchor="w", bg="lightgrey")
suggestion_label.pack(padx=10, pady=5)

# Button zum Ausführen des Codes
execute_button = tk.Button(root, text="Code ausführen", command=execute_code)
execute_button.pack(pady=10)

# Button zum Zurücksetzen der Ausgabe
reset_button = tk.Button(root, text="Ausgabe zurücksetzen", command=reset_output)
reset_button.pack(pady=10)

# Textfeld für die Ausgabe
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
output_text.pack(padx=10, pady=10)
output_text.config(state=tk.DISABLED)

# Start des Modell-Ladevorgangs
load_thread = threading.Thread(target=initialize_model)
load_thread.daemon = True
load_thread.start()

# Start der Haupt-Event-Schleife
root.mainloop()
