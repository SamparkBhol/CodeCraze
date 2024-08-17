# transformer_model.py

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class TransformerModel:
    def __init__(self, model_name: str = 'gpt2'):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
    
    def generate_code(self, prompt: str, max_length: int = 50):
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=max_length, num_return_sequences=1, pad_token_id=self.tokenizer.eos_token_id)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    def fine_tune(self, dataset, num_epochs: int = 3):
        # Fine-tuning logic here (e.g., custom code generation dataset)
        pass

# Example usage
if __name__ == "__main__":
    transformer = TransformerModel()
    code = transformer.generate_code("def hello_world():")
    print(code)
