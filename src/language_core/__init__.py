# __init__.py

"""
language_core: The core components of the custom NLP-driven programming language.

Modules included:
- lexer: Tokenizes the source code.
- parser: Parses tokens into an abstract syntax tree (AST).
- interpreter: Executes the parsed code.
- nlp_processor: Processes natural language commands using BERT/Transformers.
- compiler: Compiles source code into executable code.
- optimizer: Optimizes code using NLP-driven methods.
- error_handler: Handles errors with AI-powered explanations.
"""

__all__ = [
    "lexer",
    "parser",
    "interpreter",
    "nlp_processor",
    "compiler",
    "optimizer",
    "error_handler"
]

# Example imports to make module usage easier
from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter
from .nlp_processor import NLPProcessor
from .compiler import Compiler
from .optimizer import CodeOptimizer
from .error_handler import ErrorHandler
from .interpreter import Environment

