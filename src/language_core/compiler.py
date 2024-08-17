# compiler.py

from parser import ASTNode
from typing import List

class Compiler:
    def __init__(self):
        self.code = ""

    def compile(self, ast: ASTNode) -> str:
        self.code = ""
        self.compile_node(ast)
        return self.code

    def compile_node(self, node: ASTNode):
        if node.type == 'STATEMENTS':
            for child in node.children:
                self.compile_node(child)
        elif node.type == 'FUNCTION':
            function_name = node.children[0].value
            self.code += f"def {function_name}("
            self.compile_node(node.children[1])
            self.code += "):\n"
            self.compile_node(node.children[2])
            self.code += "\n"
        elif node.type == 'PARAMETERS':
            params = [param.value for param in node.children]
            self.code += ", ".join(params)
        elif node.type == 'RETURN':
            self.code += "    return "
            self.compile_node(node.children[0])
            self.code += "\n"
        elif node.type == 'IF':
            self.code += "if "
            self.compile_node(node.children[0])
            self.code += ":\n"
            self.compile_node(node.children[1])
            if len(node.children) > 2:
                self.code += "else:\n"
                self.compile_node(node.children[2])
        elif node.type == 'BLOCK':
            for child in node.children:
                self.code += "    "
                self.compile_node(child)
        elif node.type == 'OPERATOR':
            self.compile_node(node.children[0])
            self.code += f" {node.value} "
            self.compile_node(node.children[1])
        elif node.type == 'NUMBER':
            self.code += node.value
        elif node.type == 'IDENTIFIER':
            self.code += node.value
        else:
            raise ValueError(f"Unknown node type: {node.type}")

# Example usage
if __name__ == "__main__":
    from lexer import Lexer
    from parser import Parser

    code = """
    def foo(x):
        if x > 0:
            return x * 2
        else:
            return -x
    """

    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()

    compiler = Compiler()
    compiled_code = compiler.compile(ast)
    print(compiled_code)
