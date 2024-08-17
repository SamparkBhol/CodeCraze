# tokenizer.py

from transformers import BertTokenizer

class Tokenizer:
    def __init__(self, model_name: str = 'bert-base-uncased'):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
    
    def tokenize(self, text: str):
        return self.tokenizer.tokenize(text)
    
    def encode(self, text: str, max_length: int = 512):
        return self.tokenizer.encode(text, max_length=max_length, truncation=True)
    
    def decode(self, tokens):
        return self.tokenizer.decode(tokens)

# Example usage
if __name__ == "__main__":
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize("This is a sample text.")
    print(tokens)
