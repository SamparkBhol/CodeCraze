import unittest
from src.language_core.interpreter import Interpreter
from src.language_core.parser import Parser
from src.language_core.lexer import Lexer

class TestInterpreter(unittest.TestCase):

    def setUp(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.interpreter = Interpreter()

    def test_variable_assignment(self):
        code = "x = 10"
        tokens = self.lexer.tokenize(code)
        ast = self.parser.parse(tokens)
        result = self.interpreter.execute(ast)
        self.assertEqual(self.interpreter.environment['x'], 10)

    def test_arithmetic_operation(self):
        code = "result = 5 + 3 * 2"
        tokens = self.lexer.tokenize(code)
        ast = self.parser.parse(tokens)
        result = self.interpreter.execute(ast)
        self.assertEqual(self.interpreter.environment['result'], 11)

    def test_function_execution(self):
        code = """
        def add(a, b):
            return a + b
        result = add(3, 4)
        """
        tokens = self.lexer.tokenize(code)
        ast = self.parser.parse(tokens)
        result = self.interpreter.execute(ast)
        self.assertEqual(self.interpreter.environment['result'], 7)

    def test_conditional_execution(self):
        code = """
        x = 10
        if x > 5:
            y = 20
        else:
            y = 0
        """
        tokens = self.lexer.tokenize(code)
        ast = self.parser.parse(tokens)
        result = self.interpreter.execute(ast)
        self.assertEqual(self.interpreter.environment['y'], 20)

    def test_loop_execution(self):
        code = """
        sum = 0
        for i in range(5):
            sum += i
        """
        tokens = self.lexer.tokenize(code)
        ast = self.parser.parse(tokens)
        result = self.interpreter.execute(ast)
        self.assertEqual(self.interpreter.environment['sum'], 10)

if __name__ == "__main__":
    unittest.main()
