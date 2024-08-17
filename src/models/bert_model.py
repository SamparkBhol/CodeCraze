# bert_model.py

from transformers import BertTokenizer, BertForSequenceClassification
import torch

class BertModel:
    def __init__(self, model_name: str = 'bert-base-uncased'):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained(model_name)
    
    def run(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        outputs = self.model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1).tolist()[0]
        
        # Assuming a binary classification for simplicity
        labels = ["Negative", "Positive"]
        return {
            "label": labels[probabilities.index(max(probabilities))],
            "score": max(probabilities)
        }
    
    def fine_tune(self, dataset, num_epochs: int = 3):
        # Fine-tuning logic here (e.g., custom dataset)
        pass

# Example usage
if __name__ == "__main__":
    bert_model = BertModel()
    result = bert_model.run("This is a test sentence.")
    print(result)
