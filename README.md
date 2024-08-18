# CodeCraze

Welcome to **CodeCraze**! 🎉 This project is designed to provide an interactive playground for exploring and coding with a custom NLP-based programming language. This README will guide you through the setup, usage, and features of CodeCraze.

## 📝 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Examples](#examples)
- [How It Works](#how-it-works)
- [Contributing](#contributing)

## Introduction

**CodeCraze** is an innovative platform that allows you to write and execute code using a custom NLP-based programming language. Whether you are a developer exploring new languages or just interested in playing around with NLP-powered code execution, CodeCraze provides a user-friendly environment to test and visualize your code.

## Features

- **Interactive Playground:** Write and run code in the built-in playground.
- **Dynamic Code Execution:** See your code’s output instantly.
- **Example Code:** Start with pre-written examples to get a feel for the language.
- **Developer Profile:** Learn more about the creator of CodeCraze.

## Screenshot of Interface
![image](https://github.com/user-attachments/assets/bfa6da04-cfaf-48e2-be0b-db07519022fe)
![image](https://github.com/user-attachments/assets/f6ba004e-31e3-4f49-9676-53eee21e3e4f)
![image](https://github.com/user-attachments/assets/2127d349-2e8b-4ea8-ae79-1e1123f4b4d9)

## Setup

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, Edge)
- Basic understanding of JavaScript and HTML

### Getting Started

**Clone the Repository:**

   bash
   git clone https://github.com/your-username/CodeCraze.git
   cd CodeCraze
   
**Set Up the Environment:**

Ensure you have Python and pip installed. It's recommended to use a virtual environment for Python projects. Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install Dependencies:

**Install the necessary Python packages using pip:**

bash
Copy code
pip install -r requirements.txt
Make sure requirements.txt includes Flask and any other required packages.

**Run the Flask Backend:**

Start the Flask server to enable the backend functionalities for CodeCraze:

bash
Copy code
flask run
By default, Flask will run on http://localhost:5000. Ensure this matches the URL specified in your frontend code (playground_frontend.py).

**Open index.html in Your Browser:**

Simply open the index.html file located in the CodeCraze directory in your preferred web browser to start using CodeCraze.

You can do this by double-clicking the file or opening it through your browser's "Open File" menu.

**Accessing the Playground:**

Navigate to the "Playground" section on the website.
Use the provided textarea to write and execute your NLP commands.
The Flask backend will handle the execution and return results directly to the web interface.

**Additional Notes**
Backend Scripts: Ensure that playground_backend.py and other related backend scripts are correctly set up and running as per the Flask application. The backend handles the API requests from the frontend.

**Frontend and Backend Communication:** The frontend (HTML/JavaScript) sends requests to the backend Flask server. Make sure that the endpoints (e.g., /execute, /optimize, /nlp-command, /syntax-highlight) are correctly defined and functioning in your Flask application.

**Troubleshooting:** If you encounter any issues, check the browser console for errors and ensure the Flask server is running without issues. Check Flask logs for any server-side errors.

## Usage
    Enter Code: Write your code in the textarea under the Playground section.
    Run Code: Click the "Run Code" button to execute your code and see the output.
    View Results: The output will be displayed below the textarea.

## Examples
print("Hello, World!");
ask("What is NLP?") -> explain("Natural Language Processing involves computational techniques for analyzing and modeling human language.");

## Contribution
We welcome contributions to CodeCraze! If you’d like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.There might be a good amount of issues feel free to address it
   
