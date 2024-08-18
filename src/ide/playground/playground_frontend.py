import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
import json

class PlaygroundFrontend:
    def __init__(self, root):
        self.root = root
        self.root.title("NLP-Powered Playground")
        
        self.url = "http://localhost:5000"
        
        # Setup UI components
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True, height=20, width=60)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.run_button = tk.Button(self.root, text="Run Code", command=self.execute_code)
        self.run_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.optimize_button = tk.Button(self.root, text="Optimize Code", command=self.optimize_code)
        self.optimize_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.nlp_command_button = tk.Button(self.root, text="Run NLP Command", command=self.run_nlp_command)
        self.nlp_command_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.highlight_button = tk.Button(self.root, text="Highlight Syntax", command=self.syntax_highlight)
        self.highlight_button.pack(side=tk.LEFT, padx=10, pady=10)
    
    def execute_code(self):
        code = self.text_area.get("1.0", tk.END)
        response = self._post_request("/execute", {"source_code": code})
        messagebox.showinfo("Execution Result", response.get("message", "No message returned"))
    
    def optimize_code(self):
        code = self.text_area.get("1.0", tk.END)
        response = self._post_request("/optimize", {"source_code": code})
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.INSERT, response.get("optimized_code", "No optimized code returned"))
        messagebox.showinfo("Optimization Result", "Code optimized successfully.")
    
    def run_nlp_command(self):
        command = self.text_area.get("1.0", tk.END)
        response = self._post_request("/nlp-command", {"command": command})
        self.text_area.insert(tk.INSERT, "\n" + response.get("response", "No response returned"))
    
    def syntax_highlight(self):
        code = self.text_area.get("1.0", tk.END)
        response = self._post_request("/syntax-highlight", {"source_code": code})
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.INSERT, response.get("highlighted_code", "No highlighted code returned"))
    
    def _post_request(self, endpoint, data):
        try:
            response = requests.post(self.url + endpoint, json=data)
            return response.json()
        except Exception as e:
            return {"status": "error", "message": str(e)}

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = PlaygroundFrontend(root)
    root.mainloop()
