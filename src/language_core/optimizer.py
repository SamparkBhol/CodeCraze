# optimizer.py

from nlp_processor import NLPProcessor
from parser import ASTNode
from typing import List

class CodeOptimizer:
    def __init__(self):
        self.nlp_processor = NLPProcessor()

    def optimize(self, ast: ASTNode) -> ASTNode:
        # Example: Simplify expressions based on NLP insights
        for child in ast.children:
            if child.type == 'OPERATOR' and child.value == '+':
                left = child.children[0]
                right = child.children[1]
                if left.type == 'NUMBER' and right.type == 'NUMBER':
                    optimized_value = str(float(left.value) + float(right.value))
                    ast.replace_child(child, ASTNode('NUMBER', optimized_value))
            self.optimize(child)
        return ast

    def suggest_optimizations(self, code: str) -> List[str]:
        suggestions = []
        if "for i in range(len(" in code:
            suggestions.append("Consider using enumerate() for better performance.")
        if "if x == True:" in code:
            suggestions.append("Use 'if x:' instead of 'if x == True:'.")
        return suggestions

# Example usage
if __name__ == "__main__":
    from lexer import Lexer
    from parser import Parser

    code = """
    def add_numbers(a, b):
        return a + b
    """

    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()

    optimizer = CodeOptimizer()
    optimized_ast = optimizer.optimize(ast)
    suggestions = optimizer.suggest_optimizations(code)

    print(suggestions)
