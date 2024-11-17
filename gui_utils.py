import tkinter as tk
from tkinter import scrolledtext, Frame
from code_execution import execute_code, reset_output
from model_utils import generate_code_suggestion
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.styles import get_style_by_name
from pygments.token import Token

typing_delay = 500  # in Millisekunden
typing_timer = None
root = None

def set_root(root_widget: tk.Tk) -> None:
    """
    Setzt das globale root-Widget.

    Diese Funktion setzt das globale root-Widget, das das Hauptfenster der Anwendung darstellt.
    Dies ist notwendig, um auf das Hauptfenster von anderen Modulen aus zugreifen zu können.

    Parameter:
    ----------
    root_widget (tk.Tk): Das Hauptfenster-Widget.
    """
    global root
    root = root_widget

def create_gui(root: tk.Tk) -> tuple:
    """
    Erstellt die grafische Benutzeroberfläche.

    Diese Funktion erstellt und konfiguriert die grafische Benutzeroberfläche der Anwendung.
    Sie erstellt ein Textfeld für die Code-Eingabe, Zeilennummern, Syntaxhervorhebung,
    ein Label für Code-Vorschläge, Buttons zum Ausführen und Zurücksetzen des Codes sowie
    ein Textfeld für die Ausgabe.

    Parameter:
    ----------
    root (tk.Tk): Das Hauptfenster-Widget.

    Rückgabe:
    ---------
    tuple: Ein Tuple mit den erstellten Widgets (text_area, suggestion_label, execute_button, reset_button, output_text).
    """
    global text_area, suggestion_label, output_text

    # Textfeld für die Code-Eingabe
    text_area = scrolledtext.ScrolledText(
        root, wrap=tk.WORD, width=80, height=20, undo=True
    )
    text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    text_area.bind("<KeyRelease>", start_typing_timer)
    text_area.bind("<Control-space>", generate_code_suggestion_on_key)

    # Zeilennummern hinzufügen
    line_numbers = tk.Text(
        root,
        width=4,
        padx=10,
        takefocus=0,
        border=0,
        background="lightgrey",
        state="disabled",
        wrap="none",
    )
    line_numbers.pack(side=tk.LEFT, fill=tk.Y, padx=(10, 0))

    # Syntaxhervorhebung hinzufügen
    text_area.tag_configure("Token.Keyword", foreground="blue")
    text_area.tag_configure("Token.Keyword.Constant", foreground="blue")
    text_area.tag_configure("Token.Keyword.Declaration", foreground="blue")
    text_area.tag_configure("Token.Keyword.Namespace", foreground="blue")
    text_area.tag_configure("Token.Keyword.Pseudo", foreground="blue")
    text_area.tag_configure("Token.Keyword.Reserved", foreground="blue")
    text_area.tag_configure("Token.Keyword.Type", foreground="blue")
    text_area.tag_configure("Token.Name.Builtin", foreground="blue")
    text_area.tag_configure("Token.Name.Builtin.Pseudo", foreground="blue")
    text_area.tag_configure("Token.Name.Class", foreground="blue")
    text_area.tag_configure("Token.Name.Constant", foreground="blue")
    text_area.tag_configure("Token.Name.Decorator", foreground="blue")
    text_area.tag_configure("Token.Name.Entity", foreground="blue")
    text_area.tag_configure("Token.Name.Exception", foreground="blue")
    text_area.tag_configure("Token.Name.Function", foreground="blue")
    text_area.tag_configure("Token.Name.Label", foreground="blue")
    text_area.tag_configure("Token.Name.Namespace", foreground="blue")
    text_area.tag_configure("Token.Name.Other", foreground="blue")
    text_area.tag_configure("Token.Name.Tag", foreground="blue")
    text_area.tag_configure("Token.Name.Variable", foreground="blue")
    text_area.tag_configure("Token.Name.Variable.Class", foreground="blue")
    text_area.tag_configure("Token.Name.Variable.Global", foreground="blue")
    text_area.tag_configure("Token.Name.Variable.Instance", foreground="blue")
    text_area.tag_configure("Token.Name.Variable.Magic", foreground="blue")
    text_area.tag_configure("Token.Operator.Word", foreground="blue")
    text_area.tag_configure("Token.Comment", foreground="green")
    text_area.tag_configure("Token.Comment.Multiline", foreground="green")
    text_area.tag_configure("Token.Comment.Preproc", foreground="green")
    text_area.tag_configure("Token.Comment.Single", foreground="green")
    text_area.tag_configure("Token.Comment.Special", foreground="green")
    text_area.tag_configure("Token.Literal.String", foreground="red")
    text_area.tag_configure("Token.Literal.String.Affix", foreground="red")
    text_area.tag_configure("Token.Literal.String.Backtick", foreground="red")
    text_area.tag_configure("Token.Literal.String.Char", foreground="red")
    text_area.tag_configure("Token.Literal.String.Delimiter", foreground="red")
    text_area.tag_configure("Token.Literal.String.Doc", foreground="red")
    text_area.tag_configure("Token.Literal.String.Double", foreground="red")
    text_area.tag_configure("Token.Literal.String.Escape", foreground="red")
    text_area.tag_configure("Token.Literal.String.Heredoc", foreground="red")
    text_area.tag_configure("Token.Literal.String.Interpol", foreground="red")
    text_area.tag_configure("Token.Literal.String.Other", foreground="red")
    text_area.tag_configure("Token.Literal.String.Regex", foreground="red")
    text_area.tag_configure("Token.Literal.String.Single", foreground="red")
    text_area.tag_configure("Token.Literal.String.Symbol", foreground="red")
    text_area.tag_configure("Token.Literal.Number.Bin", foreground="purple")
    text_area.tag_configure("Token.Literal.Number.Float", foreground="purple")
    text_area.tag_configure("Token.Literal.Number.Hex", foreground="purple")
    text_area.tag_configure("Token.Literal.Number.Integer", foreground="purple")
    text_area.tag_configure("Token.Literal.Number.Integer.Long", foreground="purple")
    text_area.tag_configure("Token.Literal.Number.Oct", foreground="purple")
    text_area.tag_configure("Token.Operator", foreground="purple")
    text_area.tag_configure("Token.Operator.Word", foreground="purple")
    text_area.tag_configure("Token.Punctuation", foreground="purple")
    text_area.tag_configure("Token.Generic.Deleted", foreground="purple")
    text_area.tag_configure("Token.Generic.Emph", foreground="purple")
    text_area.tag_configure("Token.Generic.Error", foreground="purple")
    text_area.tag_configure("Token.Generic.Heading", foreground="purple")
    text_area.tag_configure("Token.Generic.Inserted", foreground="purple")
    text_area.tag_configure("Token.Generic.Output", foreground="purple")
    text_area.tag_configure("Token.Generic.Prompt", foreground="purple")
    text_area.tag_configure("Token.Generic.Strong", foreground="purple")
    text_area.tag_configure("Token.Generic.Subheading", foreground="purple")
    text_area.tag_configure("Token.Generic.Traceback", foreground="purple")

    def update_line_numbers(event=None):
        """
        Aktualisiert die Zeilennummern im Textfeld.

        Diese Funktion aktualisiert die Zeilennummern im Textfeld, basierend auf dem aktuellen Inhalt des Textfeldes.

        Parameter:
        ----------
        event: Das Ereignis, das die Aktualisierung auslöst.
        """
        line_numbers.config(state=tk.NORMAL)
        line_numbers.delete(1.0, tk.END)
        content = text_area.get(1.0, tk.END)
        line_count = content.count("\n")
        line_number_string = "\n".join(str(no) for no in range(1, line_count + 2))
        line_numbers.insert(1.0, line_number_string)
        line_numbers.config(state=tk.DISABLED)

    def highlight_syntax(event=None):
        """
        Hebt die Syntax im Textfeld hervor.

        Diese Funktion hebt die Syntax im Textfeld hervor, basierend auf dem aktuellen Inhalt des Textfeldes.

        Parameter:
        ----------
        event: Das Ereignis, das die Hervorhebung auslöst.
        """
        content = text_area.get(1.0, tk.END)
        text_area.mark_set("range_start", 1.0)
        data = content
        for token, content in lex(data, PythonLexer()):
            text_area.mark_set("range_end", f"range_start + {len(content)}c")
            text_area.tag_add(str(token), "range_start", "range_end")
            text_area.mark_set("range_start", "range_end")

    text_area.bind(
        "<KeyRelease>", lambda event: (update_line_numbers(), highlight_syntax())
    )
    text_area.bind(
        "<ButtonRelease>", lambda event: (update_line_numbers(), highlight_syntax())
    )

    # Rahmen und Label für den Code-Vorschlag
    suggestion_frame = Frame(root, bg="lightgrey", bd=2, relief="groove")
    suggestion_frame.pack(fill="x", padx=10, pady=5)

    suggestion_label = tk.Label(
        suggestion_frame,
        text="Lade Modell...",
        wraplength=700,
        justify="left",
        anchor="w",
        bg="lightgrey",
    )
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

    return text_area, suggestion_label, execute_button, reset_button, output_text

def start_typing_timer(event=None) -> None:
    """
    Startet den Timer für die Code-Vorschlagsgenerierung.

    Diese Funktion startet einen Timer, der nach einer bestimmten Verzögerung die Generierung von Code-Vorschlägen auslöst.
    Wenn der Timer bereits läuft, wird er zurückgesetzt.

    Parameter:
    ----------
    event: Das Ereignis, das den Timer startet.
    """
    global typing_timer
    if typing_timer is not None:
        root.after_cancel(typing_timer)
    typing_timer = root.after(typing_delay, delayed_generate_code_suggestion)

def delayed_generate_code_suggestion() -> None:
    """
    Generiert einen Code-Vorschlag nach einer Verzögerung.

    Diese Funktion wird nach einer Verzögerung aufgerufen, um einen Code-Vorschlag basierend auf dem aktuellen Inhalt des Textfeldes zu generieren.
    """
    input_text = text_area.get("1.0", tk.END).strip()
    if input_text:
        generate_code_suggestion(input_text, suggestion_label, root)

def generate_code_suggestion_on_key(event=None) -> None:
    """
    Generiert einen Code-Vorschlag, wenn eine bestimmte Taste gedrückt wird.

    Diese Funktion wird aufgerufen, wenn eine bestimmte Taste (z.B. Strg+Leertaste) gedrückt wird, um einen Code-Vorschlag basierend auf dem aktuellen Inhalt des Textfeldes zu generieren.

    Parameter:
    ----------
    event: Das Ereignis, das die Vorschlagsgenerierung auslöst.
    """
    input_text = text_area.get("1.0", tk.END).strip()
    if input_text:
        generate_code_suggestion(input_text, suggestion_label, root)
