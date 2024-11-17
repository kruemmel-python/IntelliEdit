import sys
import io
import tkinter as tk

output_text = None
text_area = None
root = None

def set_output_text(text_widget):
    global output_text
    output_text = text_widget

def set_text_area(text_widget):
    global text_area
    text_area = text_widget

def set_root_in_code_execution(root_widget):
    global root
    root = root_widget

def execute_code():
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
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, text)
    output_text.config(state=tk.DISABLED)

def reset_output():
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)
