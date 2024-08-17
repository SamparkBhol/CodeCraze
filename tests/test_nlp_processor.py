import unittest
from src.language_core.nlp_processor import NLPProcessor

class TestNLPProcessor(unittest.TestCase):

    def setUp(self):
        self.nlp_processor = NLPProcessor()

    def test_basic_command_processing(self):
        command = "Create a variable named count and set it to 5."
        code = self.nlp_processor.process(command)
        expected_code = "count = 5"
        self.assertEqual(code.strip(), expected_code)

    def test_function_command_processing(self):
        command = "Define a function called greet that takes a name and returns 'Hello, ' plus the name."
        code = self.nlp_processor.process(command)
        expected_code = "def greet(name):\n    return 'Hello, ' + name"
        self.assertIn("def greet", code)
        self.assertIn("return", code)

    def test_conditional_command_processing(self):
        command = "If the variable x is greater than 10, print 'Large number'."
        code = self.nlp_processor.process(command)
        expected_code = "if x > 10:\n    print('Large number')"
        self.assertIn("if x > 10", code)
        self.assertIn("print('Large number')", code)

    def test_loop_command_processing(self):
        command = "Create a loop that runs 5 times and prints the iteration number."
        code = self.nlp_processor.process(command)
        expected_code = "for i in range(5):\n    print(i)"
        self.assertIn("for i in range(5)", code)
        self.assertIn("print(i)", code)

if __name__ == "__main__":
    unittest.main()
