# 📚 API Reference

Welcome to the API reference for **My Custom Programming Language**. This document provides detailed information about the core modules and their functionalities.

## 📦 Core Modules

### 1. **Lexer**

The `Lexer` module is responsible for converting source code into tokens.

- **Functions:**
  - `tokenize(code: str) -> List[Token]`: Converts code into a list of tokens.

### 2. **Parser**

The `Parser` module converts tokens into an abstract syntax tree (AST).

- **Functions:**
  - `parse(tokens: List[Token]) -> AST`: Parses tokens into an AST.

### 3. **Interpreter**

The `Interpreter` module executes the AST.

- **Functions:**
  - `execute(ast: AST) -> Any`: Executes the AST and returns the result.

### 4. **Compiler**

The `Compiler` module compiles the AST into bytecode.

- **Functions:**
  - `compile(ast: AST) -> Bytecode`: Compiles the AST into bytecode.

### 5. **NLPProcessor**

The `NLPProcessor` module handles natural language commands.

- **Functions:**
  - `process(command: str) -> str`: Converts a natural language command into code.

## 🔗 External Libraries

This project also leverages several external libraries, including:

- **Transformers**: For BERT integration.
- **Flask**: For the IDE's backend.

For more details on these, refer to the respective documentation.
