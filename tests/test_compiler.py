import unittest
from src.language_core.compiler import Compiler
from src.language_core.parser import Parser
from src.language_core.lexer import Lexer

class TestCompiler(unittest.TestCase):

    def setUp(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.compiler = Compiler()

    def test_simple_code_compilation(self):
        code = "x = 10 + 20"
        tokens = self.lexer.tokenize(code)
        ast = self.parser.parse(tokens)
        bytecode = self.compiler.compile(ast)
        self.assertIsNotNone(bytecode)
        self.assertIn('LOAD_CONST', bytecode)

    def test_function_compilation(self):
        code = """
        def multiply(a, b):
            return a * b
        """
        tokens = self.lexer.tokenize(code)
        ast = self.parser.parse(tokens)
        bytecode = self.compiler.compile(ast)
        self.assertIn('LOAD_FAST', bytecode)
        self.assertIn('BINARY_MULTIPLY', bytecode)

    def test_conditional_compilation(self):
        code = ""
        if x > 5:
            y = 10
        else:
            y = 0
