# ide_main.py

import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from syntax_highlighting import SyntaxHighlighter
from code_completion import CodeCompletionEngine
from nlp_integration import NLPIntegration

class IDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom NLP-Powered IDE")
        self.filepath = None

        # Create the main text area
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Initialize modules
        self.highlighter = SyntaxHighlighter(self.text_area)
        self.completion_engine = CodeCompletionEngine(self.text_area)
        self.nlp_integration = NLPIntegration(self.text_area)

        # Set up menu
        self._setup_menu()

        # Bind events
        self.text_area.bind('<KeyRelease>', self._on_key_release)

    def _setup_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self._new_file)
        file_menu.add_command(label="Open", command=self._open_file)
        file_menu.add_command(label="Save", command=self._save_file)
        file_menu.add_command(label="Save As", command=self._save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        tools_menu = tk.Menu(menu_bar, tearoff=0)
        tools_menu.add_command(label="Run NLP Command", command=self._run_nlp_command)
        menu_bar.add_cascade(label="Tools", menu=tools_menu)

        self.root.config(menu=menu_bar)

    def _new_file(self):
        self.filepath = None
        self.text_area.delete(1.0, tk.END)

    def _open_file(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        self.filepath = filepath
        with open(filepath, "r") as file:
            content = file.read()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, content)
        self.highlighter.highlight()

    def _save_file(self):
        if self.filepath is None:
            self._save_file_as()
        else:
            with open(self.filepath, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Info", "File saved successfully.")

    def _save_file_as(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        self.filepath = filepath
        self._save_file()

    def _run_nlp_command(self):
        command = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
        response = self.nlp_integration.run_nlp_command(command)
        self.text_area.insert(tk.INSERT, "\n" + response)

    def _on_key_release(self, event):
        self.highlighter.highlight()
        self.completion_engine.provide_completions(event)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    ide = IDE(root)
    root.mainloop()
