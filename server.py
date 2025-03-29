from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import zipfile
import pandas as pd
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS to allow cross-origin requests

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/api/", methods=["POST"])
def csv_chatbot_api():
    if "question" not in request.form or "file" not in request.files:
        return jsonify({"error": "Missing question or file"}), 400

    question = request.form["question"]
    file = request.files["file"]
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    # Handle ZIP files
    if filename.endswith(".zip"):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(UPLOAD_FOLDER)
            extracted_files = zip_ref.namelist()
            csv_file = next((f for f in extracted_files if f.endswith(".csv")), None)
            if not csv_file:
                return jsonify({"error": "No CSV file found in ZIP"}), 400
            file_path = os.path.join(UPLOAD_FOLDER, csv_file)

    agent = create_csv_agent(OpenAI(temperature=0), file_path, verbose=True, allow_dangerous_code=True)
    response = agent.run(question)

    return jsonify({"answer": response})


# Entry point for Vercel
def handler(event, context):
    from mangum import Mangum
    asgi_app = app
    return Mangum(asgi_app)(event, context)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
