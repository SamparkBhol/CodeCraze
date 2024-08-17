import unittest
from src.language_core.parser import Parser, ParseError
from src.language_core.lexer import Lexer

class TestParser(unittest.TestCase):

    def setUp(self):
        self.lexer = Lexer()
        self.parser = Parser()

    def test_basic_expression(self):
        code = "a = 5 + 3"
        tokens = self.lexer.tokenize(code)
        ast = self.parser.parse(tokens)
        self.assertIsNotNone(ast)
        self.assertEqual(ast.type, 'Assignment')
        self.assertEqual(ast.left.value, 'a')

    def test_function_definition(self):
        code = "def greet(name): return 'Hello, ' + name"
        tokens = self.lexer.tokenize(code)
        ast = self.parser.parse(tokens)
        self.assertIsNotNone(ast)
        self.assertEqual(ast.type, 'FunctionDef')
        self.assertEqual(ast.name, 'greet')

    def test_if_statement(self):
        code = "if x > 10: print('Greater')"
        tokens = self.lexer.tokenize(code)
        ast = self.parser.parse(tokens)
        self.assertIsNotNone(ast)
        self.assertEqual(ast.type, 'IfStatement')
        self.assertEqual(ast.condition.type, 'BinaryOp')

    def test_syntax_error(self):
        code = "def func( return 5"
        tokens = self.lexer.tokenize(code)
        with self.assertRaises(ParseError):
            self.parser.parse(tokens)

    def test_nested_statements(self):
        code = """
        if x > 10:
            if y < 5:
                print('Nested')
        """
        tokens = self.lexer.tokenize(code)
        ast = self.parser.parse(tokens)
        self.assertIsNotNone(ast)
        self.assertEqual(ast.type, 'IfStatement')
        self.assertEqual(ast.body[0].type, 'IfStatement')

if __name__ == "__main__":
    unittest.main()
