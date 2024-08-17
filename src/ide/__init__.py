# __init__.py

"""
ide: Custom Integrated Development Environment (IDE) for the NLP-driven programming language.

Modules included:
- ide_main: Entry point for the custom IDE.
- syntax_highlighting: Handles syntax highlighting in the IDE.
- code_completion: AI-driven autocompletion engine.
- nlp_integration: Integrates NLP commands into the IDE.
"""

__all__ = [
    "ide_main",
    "syntax_highlighting",
    "code_completion",
    "nlp_integration"
]

# Example imports to make module usage easier
from .ide_main import IDE
from .syntax_highlighting import SyntaxHighlighter
from .code_completion import CodeCompletionEngine
from .nlp_integration import NLPIntegration
