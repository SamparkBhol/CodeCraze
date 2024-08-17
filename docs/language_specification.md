# 📚 Language Specification

This document details the specifications of the **My Custom Programming Language**.

## Syntax Overview

The syntax is designed to be simple yet powerful. Here’s an example of a function definition:

```my-lang
def greet(name):
    return "Hello, " + name
```

### Data Types

- **Integers**: `int a = 5`
- **Strings**: `str greeting = "Hello!"`
- **Lists**: `list numbers = [1, 2, 3]`
- **Dictionaries**: `dict person = {"name": "Alice", "age": 30}`

### Control Flow

- **If Statements**: `if x > 10:`
- **For Loops**: `for i in range(5):`
- **While Loops**: `while x < 10:`

### Functions

Functions are defined using the `def` keyword:

```my-lang
def add(a, b):
    return a + b
```

## Error Handling

Error handling is done using the `try-except` structure:

```my-lang
try:
    risky_operation()
except:
    handle_error()
```
