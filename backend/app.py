from flask_cors import CORS
from flask import Flask, request, jsonify, send_file
from t5 import generate_qa_pairs
from tts import text_to_speech
from transformers import pipeline
import numpy as np
from PIL import Image
import os

from pdf2image import convert_from_bytes
import easyocr
import io

from flask import Flask, request, jsonify
from flask_cors import CORS
from roadmap_generator import generate_learning_roadmap


app = Flask(__name__)
CORS(app)

@app.route("/generate-roadmap", methods=["POST"])
def generate_roadmap():
    data = request.json
    topic = data.get("topic")

    if not topic:
        return jsonify({"error": "No topic provided"}), 400

    roadmap = generate_learning_roadmap(topic)
    return jsonify({"roadmap": roadmap})

app.config["AUDIO_FOLDER"] = "."
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

reader = easyocr.Reader(['en'])

@app.route('/pdf-ocr', methods=['POST'])
def pdf_ocr():
    file = request.files['file']
    images = convert_from_bytes(file.read())  # list of PIL images

    full_text = ""

    for page_image in images:
        # ✅ Convert PIL image to NumPy array
        np_image = np.array(page_image)

        # ✅ Now pass to EasyOCR
        result = reader.readtext(np_image, detail=0)
        full_text += "\n".join(result) + "\n\n"

    return jsonify({ "extracted_text": full_text.strip() })
    
    

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400

    summary = summarizer(text, max_length=700, min_length=250, do_sample=False)
    return jsonify({"summary": summary[0]['summary_text']})


@app.route("/generate-qa", methods=["POST"])
def qa():
    data = request.get_json()
    text = data.get("text", "")
    num_questions = int(data.get("num_questions", 5))
    
    if not text:
        return jsonify({"error": "No text provided"}), 400  
    
    qa_pairs = generate_qa_pairs(text, num_questions)
    return jsonify({"qa_pairs": qa_pairs})

@app.route("/text-to-speech", methods=["POST"])
def tts():
    data = request.get_json()
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    filename = "output.mp3"
    text_to_speech(text, filename)
    
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
