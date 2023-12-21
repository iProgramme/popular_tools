from flask import Flask, request, jsonify
from PIL import Image
import os
import cv2
import numpy as np
import uuid  # 用于生成唯一的文件名

app = Flask(__name__, static_folder='/')

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(file_path):
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) > 0:
        x, y, w, h = faces[0]
        face_image = image[y:y+h, x:x+w]

        # 生成唯一的文件名
        unique_filename = str(uuid.uuid4()) + '.jpg'

        # 保存抠图后的人脸图像（保存为彩色图像）
        face_image_path = os.path.join(UPLOAD_FOLDER, unique_filename)
        cv2.imwrite(face_image_path, face_image)

        return face_image_path
    else:
        return None

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        face_image_path = process_image(file_path)

        if face_image_path:
            return jsonify({'face_image': face_image_path})
        else:
            return jsonify({'error': 'No face detected in the image'}), 400
    else:
        return jsonify({'error': 'Invalid file format'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
