import unittest
from src.ide.code_completion import CodeCompletionEngine

class TestCodeCompletion(unittest.TestCase):

    def setUp(self):
        self.code_completion = CodeCompletionEngine()

    def test_basic_completion(self):
        context = "pri"
        completions = self.code_completion.suggest(context)
        self.assertIn("print", completions)

    def test_function_completion(self):
        context = "def greet("
        completions = self.code_completion.suggest(context)
        self.assertIn("name", completions)

    def test_variable_completion(self):
        context = "my_var = 10\nmy_"
        completions = self.code_completion.suggest(context)
        self.assertIn("my_var", completions)

    def test_method_completion(self):
        context = "my_list = []\nmy_list.ap"
        completions = self.code_completion.suggest(context)
        self.assertIn("append", completions)

    def test_snippet_completion(self):
        context = "for i in range("
        completions = self.code_completion.suggest(context)
        self.assertIn("len(", completions)

if __name__ == "__main__":
    unittest.main()
