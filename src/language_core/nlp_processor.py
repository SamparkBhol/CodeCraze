# nlp_processor.py

import torch
from transformers import BertTokenizer, BertForSequenceClassification
from typing import List

class NLPProcessor:
    def __init__(self, model_name: str = 'bert-base-uncased'):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained(model_name)
        self.model.eval()

    def classify(self, text: str) -> str:
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=1).item()
        return 'positive' if prediction == 1 else 'negative'

    def extract_entities(self, text: str) -> List[str]:
        tokens = self.tokenizer.tokenize(text)
        inputs = self.tokenizer.encode(text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=-1)
        entities = [tokens[i] for i, pred in enumerate(predictions[0]) if pred == 1]
        return entities

    def generate_code(self, text: str) -> str:
        # Example: Translate natural language to code
        if "create a function" in text:
            function_name = text.split("called")[1].split()[0]
            return f"def {function_name}():\n    pass\n"
        elif "add" in text and "return" in text:
            numbers = [int(word) for word in text.split() if word.isdigit()]
            return f"def add_numbers():\n    return {numbers[0]} + {numbers[1]}\n"
        else:
            return "# Could not interpret the command"

# Example usage
if __name__ == "__main__":
    processor = NLPProcessor()

    print("Classification:", processor.classify("This is a great product!"))
    print("Entities:", processor.extract_entities("John bought 300 shares of Acme Corp."))
    print("Generated Code:", processor.generate_code("create a function called add that adds 2 numbers and return result"))
