import unittest
from src.language_core.lexer import Lexer, TokenType

class TestLexer(unittest.TestCase):

    def setUp(self):
        self.lexer = Lexer()

    def test_simple_tokens(self):
        code = "print('Hello, World!')"
        tokens = self.lexer.tokenize(code)
        self.assertEqual(len(tokens), 5)
        self.assertEqual(tokens[0].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[1].type, TokenType.LPAREN)
        self.assertEqual(tokens[2].type, TokenType.STRING)
        self.assertEqual(tokens[3].type, TokenType.RPAREN)
        self.assertEqual(tokens[4].type, TokenType.EOF)

    def test_operators(self):
        code = "a = 5 + 3 * 2"
        tokens = self.lexer.tokenize(code)
        self.assertEqual(len(tokens), 7)
        self.assertEqual(tokens[0].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[1].type, TokenType.ASSIGN)
        self.assertEqual(tokens[2].type, TokenType.INTEGER)
        self.assertEqual(tokens[3].type, TokenType.PLUS)
        self.assertEqual(tokens[4].type, TokenType.INTEGER)
        self.assertEqual(tokens[5].type, TokenType.STAR)
        self.assertEqual(tokens[6].type, TokenType.INTEGER)

    def test_invalid_token(self):
        code = "a = $5"
        with self.assertRaises(SyntaxError):
            self.lexer.tokenize(code)

    def test_multiline_code(self):
        code = """
        x = 10
        y = 20
        print(x + y)
        """
        tokens = self.lexer.tokenize(code)
        self.assertGreater(len(tokens), 10)
        self.assertTrue(all(token.type != TokenType.INVALID for token in tokens))

if __name__ == "__main__":
    unittest.main()
