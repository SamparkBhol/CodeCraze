# deploy_playground.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route("/execute", methods=["POST"])
def execute_code():
    try:
        code = request.json.get("code")
        if not code:
            return jsonify({"error": "No code provided"}), 400

        with open("temp_code.py", "w") as file:
            file.write(code)

        result = subprocess.run(["python3", "temp_code.py"], capture_output=True, text=True)
        os.remove("temp_code.py")
        
        if result.returncode != 0:
            return jsonify({"error": result.stderr.strip()}), 400

        return jsonify({"output": result.stdout.strip()})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"status": "Running"})

def start_playground(host="0.0.0.0", port=5000):
    app.run(host=host, port=port)

if __name__ == "__main__":
    start_playground()
    print("Playground deployed successfully.")
