# interpreter.py

from parser import ASTNode, Parser
from lexer import Lexer
from typing import Any, Dict

class Environment:
    def __init__(self):
        self.variables: Dict[str, Any] = {}
        self.functions: Dict[str, ASTNode] = {}

    def get_variable(self, name: str) -> Any:
        if name in self.variables:
            return self.variables[name]
        else:
            raise NameError(f"Variable '{name}' is not defined")

    def set_variable(self, name: str, value: Any):
        self.variables[name] = value

    def get_function(self, name: str) -> ASTNode:
        if name in self.functions:
            return self.functions[name]
        else:
            raise NameError(f"Function '{name}' is not defined")

    def set_function(self, name: str, body: ASTNode):
        self.functions[name] = body

class Interpreter:
    def __init__(self, environment: Environment):
        self.environment = environment

    def interpret(self, node: ASTNode) -> Any:
        if node.type == 'STATEMENTS':
            for child in node.children:
                self.interpret(child)
        elif node.type == 'BLOCK':
            for child in node.children:
                self.interpret(child)
        elif node.type == 'IF':
            condition = self.interpret(node.children[0])
            if condition:
                return self.interpret(node.children[1])
            elif len(node.children) > 2:
                return self.interpret(node.children[2])
        elif node.type == 'FUNCTION':
            function_name = node.children[0].value
            self.environment.set_function(function_name, node)
        elif node.type == 'RETURN':
            return self.interpret(node.children[0])
        elif node.type == 'IDENTIFIER':
            return self.environment.get_variable(node.value)
        elif node.type == 'NUMBER':
            return float(node.value)
        elif node.type == 'OPERATOR':
            left = self.interpret(node.children[0])
            right = self.interpret(node.children[1])
            if node.value == '+':
                return left + right
            elif node.value == '-':
                return left - right
            elif node.value == '*':
                return left * right
            elif node.value == '/':
                return left / right
        else:
            raise ValueError(f"Unknown node type: {node.type}")

    def call_function(self, name: str, args: List[Any]) -> Any:
        function_node = self.environment.get_function(name)
        parameter_names = [param.value for param in function_node.children[1].children]
        if len(parameter_names) != len(args):
            raise TypeError(f"Expected {len(parameter_names)} arguments, got {len(args)}")
        local_env = Environment()
        for param_name, arg in zip(parameter_names, args):
            local_env.set_variable(param_name, arg)
        interpreter = Interpreter(local_env)
        result = interpreter.interpret(function_node.children[2])
        return result

# Example usage
if __name__ == "__main__":
    code = """
    def foo(x):
        if x > 0:
            return x * 2
        else:
            return -x

    result = foo(10)
    """

    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    
    env = Environment()
    interpreter = Interpreter(env)
    interpreter.interpret(ast)

    print(env.get_variable("result"))
