# syntax_highlighting.py

import re
import tkinter as tk
from typing import Dict, Tuple

class SyntaxHighlighter:
    def __init__(self, text_widget: tk.Text):
        self.text_widget = text_widget
        self._setup_tags()

    def _setup_tags(self):
        # Define tags for syntax highlighting
        self.text_widget.tag_configure("keyword", foreground="blue")
        self.text_widget.tag_configure("function", foreground="darkgreen")
        self.text_widget.tag_configure("string", foreground="orange")
        self.text_widget.tag_configure("comment", foreground="gray")

    def highlight(self):
        # Remove existing tags
        for tag in self.text_widget.tag_names():
            self.text_widget.tag_remove(tag, "1.0", tk.END)

        # Apply syntax highlighting
        code = self.text_widget.get("1.0", tk.END)
        self._highlight_keywords(code)
        self._highlight_strings(code)
        self._highlight_comments(code)
        self._highlight_functions(code)

    def _highlight_keywords(self, code: str):
        keywords = ["def", "return", "if", "else", "for", "while", "import", "from", "class"]
        keyword_pattern = r'\b(' + '|'.join(keywords) + r')\b'
        for match in re.finditer(keyword_pattern, code):
            start, end = self._get_index_range(match.span())
            self.text_widget.tag_add("keyword", start, end)

    def _highlight_strings(self, code: str):
        string_pattern = r'(".*?"|\'.*?\')'
        for match in re.finditer(string_pattern, code):
            start, end = self._get_index_range(match.span())
            self.text_widget.tag_add("string", start, end)

    def _highlight_comments(self, code: str):
        comment_pattern = r'(#.*?$)'
        for match in re.finditer(comment_pattern, code, re.MULTILINE):
            start, end = self._get_index_range(match.span())
            self.text_widget.tag_add("comment", start, end)

    def _highlight_functions(self, code: str):
        function_pattern = r'\bdef\b\s*(\w+)'
        for match in re.finditer(function_pattern, code):
            start, end = self._get_index_range(match.span(1))
            self.text_widget.tag_add("function", start, end)

    def _get_index_range(self, span: Tuple[int, int]) -> Tuple[str, str]:
        start = f"1.0+{span[0]}c"
        end = f"1.0+{span[1]}c"
        return start, end
