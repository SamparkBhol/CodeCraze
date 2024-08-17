# model_loader.py

from models.bert_model import BertModel
from models.transformer_model import TransformerModel
from language_core.optimizer import CodeOptimizer
from language_core.syntax_highlighting import SyntaxHighlighter

class ModelLoader:
    def __init__(self):
        self.bert_model = None
        self.transformer_model = None
        self.code_optimizer = None
        self.syntax_highlighter = None
    
    def load_bert_model(self):
        if self.bert_model is None:
            self.bert_model = BertModel()
        return self.bert_model
    
    def load_transformer_model(self):
        if self.transformer_model is None:
            self.transformer_model = TransformerModel()
        return self.transformer_model
    
    def load_optimizer(self):
        if self.code_optimizer is None:
            self.code_optimizer = CodeOptimizer()
        return self.code_optimizer
    
    def load_syntax_highlighter(self):
        if self.syntax_highlighter is None:
            self.syntax_highlighter = SyntaxHighlighter()
        return self.syntax_highlighter

# Example usage
if __name__ == "__main__":
    loader = ModelLoader()
    bert_model = loader.load_bert_model()
    transformer = loader.load_transformer_model()
