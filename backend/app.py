from flask import Flask, request, jsonify
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

AZURE_ENDPOINT = os.environ.get("AZURE_ENDPOINT")
AZURE_KEY = os.environ.get("AZURE_KEY")

document_analysis_client = DocumentAnalysisClient(
    endpoint=AZURE_ENDPOINT,
    credential=AzureKeyCredential(AZURE_KEY)
)

@app.route('/')
def home():
    return "Welcome to the Azure AI Document Analysis Service"

@app.route('/extract-text', methods=['POST'])
def extract_text():
    image = request.files['image']
    poller = document_analysis_client.begin_analyze_document(
        "prebuilt-read",
        image
    )
    result = poller.result()
    
    text = []
    for page in result.pages:
        for line in page.lines:
            text.append(line.content)

    extracted_text = " ".join(text)
    print(f"Extracted Text: {extracted_text}")  # Log the extracted text
    return jsonify({"text": extracted_text})

if __name__ == '__main__':
    app.run(debug=True)