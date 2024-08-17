# parser.py

from lexer import Token, TokenType
from typing import List, Union, Optional

class ASTNode:
    def __init__(self, type_: str, value: Optional[str] = None):
        self.type = type_
        self.value = value
        self.children: List[ASTNode] = []

    def add_child(self, node: 'ASTNode'):
        self.children.append(node)

    def __repr__(self):
        return f'ASTNode({self.type}, {self.value}, {self.children})'

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current_token_index = 0

    def current_token(self) -> Token:
        return self.tokens[self.current_token_index]

    def next_token(self) -> Token:
        self.current_token_index += 1
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        else:
            return Token(TokenType.SYMBOL, '', self.tokens[-1].line, self.tokens[-1].column)  # End of input

    def parse(self) -> ASTNode:
        return self.parse_statements()

    def parse_statements(self) -> ASTNode:
        root = ASTNode('STATEMENTS')
        while self.current_token().type != TokenType.SYMBOL or self.current_token().value != '':
            stmt = self.parse_statement()
            root.add_child(stmt)
        return root

    def parse_statement(self) -> ASTNode:
        token = self.current_token()

        if token.type == TokenType.KEYWORD:
            if token.value == 'if':
                return self.parse_if_statement()
            elif token.value == 'def':
                return self.parse_function_definition()
            elif token.value == 'return':
                return self.parse_return_statement()
        
        return self.parse_expression()

    def parse_if_statement(self) -> ASTNode:
        node = ASTNode('IF')
        self.next_token()  # Consume 'if'
        node.add_child(self.parse_expression())  # Parse condition
        node.add_child(self.parse_block())       # Parse then block
        if self.current_token().value == 'else':
            self.next_token()  # Consume 'else'
            node.add_child(self.parse_block())   # Parse else block
        return node

    def parse_function_definition(self) -> ASTNode:
        node = ASTNode('FUNCTION')
        self.next_token()  # Consume 'def'
        node.add_child(ASTNode('IDENTIFIER', self.current_token().value))  # Function name
        self.next_token()  # Consume function name
        self.next_token()  # Consume '('
        node.add_child(self.parse_parameters())
        self.next_token()  # Consume ')'
        node.add_child(self.parse_block())  # Parse function body
        return node

    def parse_parameters(self) -> ASTNode:
        node = ASTNode('PARAMETERS')
        while self.current_token().type != TokenType.SYMBOL or self.current_token().value != ')':
            if self.current_token().type == TokenType.IDENTIFIER:
                node.add_child(ASTNode('PARAMETER', self.current_token().value))
            self.next_token()
        return node

    def parse_return_statement(self) -> ASTNode:
        node = ASTNode('RETURN')
        self.next_token()  # Consume 'return'
        node.add_child(self.parse_expression())
        return node

    def parse_block(self) -> ASTNode:
        node = ASTNode('BLOCK')
        self.next_token()  # Consume '{' or start of block
        while self.current_token().type != TokenType.SYMBOL or self.current_token().value != '}':
            node.add_child(self.parse_statement())
        self.next_token()  # Consume '}' or end of block
        return node

    def parse_expression(self) -> ASTNode:
        return self.parse_term()

    def parse_term(self) -> ASTNode:
        node = self.parse_factor()
        while self.current_token().type == TokenType.OPERATOR and self.current_token().value in ('+', '-'):
            operator = ASTNode('OPERATOR', self.current_token().value)
            self.next_token()
            operator.add_child(node)
            operator.add_child(self.parse_factor())
            node = operator
        return node

    def parse_factor(self) -> ASTNode:
        node = self.parse_atom()
        while self.current_token().type == TokenType.OPERATOR and self.current_token().value in ('*', '/'):
            operator = ASTNode('OPERATOR', self.current_token().value)
            self.next_token()
            operator.add_child(node)
            operator.add_child(self.parse_atom())
            node = operator
        return node

    def parse_atom(self) -> ASTNode:
        token = self.current_token()

        if token.type == TokenType.NUMBER:
            self.next_token()
            return ASTNode('NUMBER', token.value)
        elif token.type == TokenType.IDENTIFIER:
            self.next_token()
            return ASTNode('IDENTIFIER', token.value)
        elif token.type == TokenType.STRING:
            self.next_token()
            return ASTNode('STRING', token.value)
        elif token.type == TokenType.SYMBOL and token.value == '(':
            self.next_token()
            expr = self.parse_expression()
            self.next_token()  # Consume ')'
            return expr
        else:
            raise SyntaxError(f'Unexpected token {token.value} at line {token.line}, column {token.column}')

# Example usage
if __name__ == "__main__":
    from lexer import Lexer

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
    print(ast)
