# error_handler.py

from typing import Optional
from transformers import pipeline

class ErrorHandler:
    def __init__(self, model_name: str = 'bert-base-uncased'):
        self.nlp = pipeline("text-generation", model=model_name)

    def handle_syntax_error(self, message: str) -> str:
        explanation = self.nlp(f"Explain the following syntax error: {message}")[0]['generated_text']
        return f"Syntax Error: {message}\nExplanation: {explanation}"

    def handle_runtime_error(self, message: str) -> str:
        explanation = self.nlp(f"Explain the following runtime error: {message}")[0]['generated_text']
        return f"Runtime Error: {message}\nExplanation: {explanation}"

    def handle_name_error(self, name: str) -> str:
        suggestion = f"Did you mean '{name}'? Check if it is defined correctly."
        return f"NameError: '{name}' is not defined.\nSuggestion: {suggestion}"

# Example usage
if __name__ == "__main__":
    handler = ErrorHandler()

    try:
        eval("x === 5")
    except SyntaxError as e:
        print(handler.handle_syntax_error(str(e)))

    try:
        eval("5 / 0")
    except ZeroDivisionError as e:
        print(handler.handle_runtime_error(str(e)))

    try:
        eval("undefined_variable")
    except NameError as e:
        print(handler.handle_name_error("undefined_variable"))
