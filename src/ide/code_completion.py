# code_completion.py

import tkinter as tk
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from typing import List

class CodeCompletionEngine:
    def __init__(self, text_widget: tk.Text):
        self.text_widget = text_widget
        self.model_name = "gpt2"
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)
        self.model.eval()

    def provide_completions(self, event):
        current_text = self.text_widget.get("1.0", tk.INSERT)
        if event.keysym == "space" and len(current_text.strip()) > 0:
            prompt = self._get_prompt()
            completion = self._generate_completion(prompt)
            self._insert_completion(completion)

    def _get_prompt(self) -> str:
        current_line = self.text_widget.get("insert linestart", "insert lineend")
        return current_line.strip()

    def _generate_completion(self, prompt: str) -> str:
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=50, num_return_sequences=1, pad_token_id=self.tokenizer.eos_token_id)
        completion = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return completion[len(prompt):]

    def _insert_completion(self, completion: str):
        self.text_widget.insert(tk.INSERT, completion)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    text_area = tk.Text(root)
    text_area.pack(fill=tk.BOTH, expand=1)

    completion_engine = CodeCompletionEngine(text_area)
    text_area.bind('<KeyRelease>', completion_engine.provide_completions)

    root.mainloop()
