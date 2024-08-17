# nlp_integration.py

import tkinter as tk
from transformers import pipeline

class NLPIntegration:
    def __init__(self, text_widget: tk.Text):
        self.text_widget = text_widget
        self.model_name = "bert-base-uncased"
        self.nlp = pipeline("text-classification", model=self.model_name)

    def run_nlp_command(self, command: str) -> str:
        # Example NLP task: Sentiment analysis on the command
        results = self.nlp(command)
        sentiment = results[0]['label']
        confidence = results[0]['score']
        return f"Command: {command}\nSentiment: {sentiment} (Confidence: {confidence:.2f})"

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    text_area = tk.Text(root)
    text_area.pack(fill=tk.BOTH, expand=1)

    nlp_integration = NLPIntegration(text_area)

    def run_command():
        command = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)
        response = nlp_integration.run_nlp_command(command)
        text_area.insert(tk.INSERT, "\n" + response)

    run_button = tk.Button(root, text="Run NLP Command", command=run_command)
    run_button.pack()

    root.mainloop()
