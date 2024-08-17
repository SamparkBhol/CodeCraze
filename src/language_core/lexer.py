# lexer.py

import re
from typing import List, Tuple

# Token types
class TokenType:
    KEYWORD = 'KEYWORD'
    IDENTIFIER = 'IDENTIFIER'
    OPERATOR = 'OPERATOR'
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    SYMBOL = 'SYMBOL'
    COMMENT = 'COMMENT'
    WHITESPACE = 'WHITESPACE'

# Token class
class Token:
    def __init__(self, type: str, value: str, line: int, column: int):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f'Token({self.type}, {self.value}, {self.line}, {self.column})'

# Lexer class
class Lexer:
    def __init__(self, code: str):
        self.code = code
        self.tokens: List[Token] = []
        self.current_line = 1
        self.current_column = 1

    def tokenize(self) -> List[Token]:
        token_specs = [
            (TokenType.KEYWORD, r'\b(if|else|while|for|return|import|from|as|def|class|try|except)\b'),
            (TokenType.IDENTIFIER, r'[a-zA-Z_]\w*'),
            (TokenType.OPERATOR, r'[+\-*/%=&|<>!]+'),
            (TokenType.NUMBER, r'\d+(\.\d*)?'),
            (TokenType.STRING, r'\".*?\"|\'.*?\''),
            (TokenType.SYMBOL, r'[(){}\[\],.:;]'),
            (TokenType.COMMENT, r'#.*'),
            (TokenType.WHITESPACE, r'\s+')
        ]
        
        token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specs)
        get_token = re.compile(token_regex).match

        pos = 0
        match = get_token(self.code)
        while match is not None:
            type_ = match.lastgroup
            value = match.group(type_)
            if type_ == TokenType.WHITESPACE:
                if '\n' in value:
                    self.current_line += value.count('\n')
                    self.current_column = 1
                else:
                    self.current_column += len(value)
            else:
                if type_ != TokenType.COMMENT:
                    token = Token(type_, value, self.current_line, self.current_column)
                    self.tokens.append(token)
                self.current_column += len(value)
            pos = match.end()
            match = get_token(self.code, pos)

        if pos != len(self.code):
            raise SyntaxError(f'Unexpected character {self.code[pos]} at line {self.current_line}, column {self.current_column}')
        
        return self.tokens

# Example usage
if __name__ == "__main__":
    code = """
    def foo(x):
        if x > 0:
            return x * 2
        else:
            return -x
    """

    lexer = Lexer(code)
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)
