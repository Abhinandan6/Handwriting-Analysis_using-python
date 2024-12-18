from flask import Flask, request, jsonify
import cv2
import pytesseract
from PIL import Image, ImageEnhance
import numpy as np

app = Flask(__name__)

@app.route('/compare', methods=['POST'])
def compare_handwriting():
    # Get uploaded images from the request
    img1 = request.files['image1']
    img2 = request.files['image2']
    # Load and process images here...
    similarity = 95.0  # Example similarity
    return jsonify({'similarity': f'{similarity:.2f}%'})

@app.route('/extract-text', methods=['POST'])
def extract_text():
    img = request.files['image']
    # Load and process image here...
    text = "Sample extracted text."
    return jsonify({'text': text})

if __name__ == "__main__":
    app.run(debug=True)
