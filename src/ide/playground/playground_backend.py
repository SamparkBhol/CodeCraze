from flask import Flask, request, jsonify
import requests
from models.model_loader import ModelLoader
from models.tokenizer import Tokenizer
from language_core.interpreter import Interpreter
from language_core.error_handler import ErrorHandler
from concurrent.futures import ThreadPoolExecutor
import logging

app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=5)

# Initialize components
model_loader = ModelLoader()
tokenizer = Tokenizer()
interpreter = Interpreter()
error_handler = ErrorHandler()

@app.route('/execute', methods=['POST'])
def execute_code():
    try:
        data = request.json
        source_code = data['source_code']
        
        # Tokenize and interpret code asynchronously
        tokens = tokenizer.tokenize(source_code)
        ast = interpreter.parse(tokens)
        result = executor.submit(interpreter.execute, ast).result()
        
        return jsonify({"status": "success", "message": result})
    
    except Exception as e:
        error_message = error_handler.handle_runtime_error(str(e))
        logging.error(f"Error during code execution: {error_message}")
        return jsonify({"status": "error", "message": error_message})

@app.route('/nlp-command', methods=['POST'])
def run_nlp_command():
    try:
        data = request.json
        command = data['command']
        
        # Process command with NLP model
        nlp_processor = model_loader.load_bert_model()
        response = nlp_processor.run(command)
        
        return jsonify({"status": "success", "response": response})
    
    except Exception as e:
        error_message = error_handler.handle_runtime_error(str(e))
        logging.error(f"Error during NLP command processing: {error_message}")
        return jsonify({"status": "error", "message": error_message})

@app.route('/optimize', methods=['POST'])
def optimize_code():
    try:
        data = request.json
        source_code = data['source_code']
        
        # Optimize code
        optimizer = model_loader.load_optimizer()
        optimized_code = optimizer.optimize(source_code)
        
        return jsonify({"status": "success", "optimized_code": optimized_code})
    
    except Exception as e:
        error_message = error_handler.handle_runtime_error(str(e))
        logging.error(f"Error during code optimization: {error_message}")
        return jsonify({"status": "error", "message": error_message})

@app.route('/syntax-highlight', methods=['POST'])
def syntax_highlight():
    try:
        data = request.json
        source_code = data['source_code']
        
        # Highlight syntax
        highlighter = model_loader.load_syntax_highlighter()
        highlighted_code = highlighter.highlight(source_code)
        
        return jsonify({"status": "success", "highlighted_code": highlighted_code})
    
    except Exception as e:
        error_message = error_handler.handle_runtime_error(str(e))
        logging.error(f"Error during syntax highlighting: {error_message}")
        return jsonify({"status": "error", "message": error_message})

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.json
        question = data.get('question')
        
        # Fetch data from Wikipedia
        response = requests.get(f'https://en.wikipedia.org/api/rest_v1/page/summary/{question}')
        if response.status_code == 200:
            data = response.json()
            return jsonify({"status": "success", "response": data.get('extract', 'No information found.')})
        return jsonify({"status": "error", "message": 'Error retrieving information.'})
    
    except Exception as e:
        error_message = error_handler.handle_runtime_error(str(e))
        logging.error(f"Error during question retrieval: {error_message}")
        return jsonify({"status": "error", "message": error_message})

if __name__ == '__main__':
    app.run(debug=True)
