import sys
import io
import tkinter as tk

output_text = None
text_area = None
root = None

def set_output_text(text_widget):
    """
    Setzt das globale ``output_text`` auf das gegebene Text-Widget.

    Diese Funktion setzt das globale ``output_text`` auf das gegebene Text-Widget, das als Ausgabebereich verwendet wird.
    Dies ist notwendig, um die Ausgabe des ausgeführten Codes anzuzeigen.

    Parameter:
    ----------
    text_widget (tk.Text): Das Text-Widget, das als Ausgabebereich verwendet wird.
    """
    global output_text
    output_text = text_widget

def set_text_area(text_widget):
    """
    Setzt das globale ``text_area`` auf das gegebene Text-Widget.

    Diese Funktion setzt das globale ``text_area`` auf das gegebene Text-Widget, das als Eingabebereich verwendet wird.
    Dies ist notwendig, um den eingegebenen Code zu erfassen und auszuführen.

    Parameter:
    ----------
    text_widget (tk.Text): Das Text-Widget, das als Eingabebereich verwendet wird.
    """
    global text_area
    text_area = text_widget

def set_root_in_code_execution(root_widget):
    """
    Setzt das globale ``root`` auf das gegebene Root-Widget.

    Diese Funktion setzt das globale ``root`` auf das gegebene Root-Widget der Tkinter-Anwendung.
    Dies ist notwendig, um auf das Hauptfenster von anderen Modulen aus zugreifen zu können.

    Parameter:
    ----------
    root_widget (tk.Tk): Das Root-Widget der Tkinter-Anwendung.
    """
    global root
    root = root_widget

def execute_code():
    """
    Führt den im ``text_area`` enthaltenen Code aus und zeigt die Ausgabe im ``output_text`` an.

    Diese Funktion führt den im ``text_area`` enthaltenen Code aus und zeigt die Ausgabe im ``output_text`` an.
    Sie fängt sowohl die Standardausgabe als auch die Fehlerausgabe ab und zeigt sie im Ausgabebereich an.
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
        error_message = f"Fehler bei der Ausführung: {str(e)}\n"
        root.after(0, lambda: update_output_text(error_message))
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

def update_output_text(text):
    """
    Aktualisiert den Text im ``output_text`` Widget.

    Diese Funktion aktualisiert den Text im ``output_text`` Widget, indem sie den gegebenen Text einfügt.
    Sie stellt sicher, dass das Widget bearbeitbar ist, bevor der Text eingefügt wird, und deaktiviert die Bearbeitung danach wieder.

    Parameter:
    ----------
    text (str): Der Text, der in das ``output_text`` Widget eingefügt werden soll.
    """
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, text)
    output_text.config(state=tk.DISABLED)

def reset_output():
    """
    Setzt den Text im ``output_text`` Widget zurück.

    Diese Funktion setzt den Text im ``output_text`` Widget zurück, indem sie den gesamten Inhalt löscht.
    Sie stellt sicher, dass das Widget bearbeitbar ist, bevor der Inhalt gelöscht wird, und deaktiviert die Bearbeitung danach wieder.
    """
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)
