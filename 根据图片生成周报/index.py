from flask import Flask, request, jsonify
# from pymongo import MongoClient
from PIL import Image
import pytesseract
import io
import re

app = Flask(__name__, static_folder='/')

# 连接到MongoDB数据库
# client = MongoClient('mongodb://localhost:27017/')
# db = client['image_processing_db']
# collection = db['processed_images']

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        image_file = request.files['image']

        # 保存上传的图片
        image = Image.open(image_file)
        image.save('uploaded_image.png')

        # 识别图片内容并进行过滤
        image_text = pytesseract.image_to_string(image, lang='chi_sim')
        filtered_text = re.sub(r'[A-Za-z:]', '', image_text)

        # 存储到MongoDB
        document = {'original_text': image_text, 'filtered_text': filtered_text}
        # result = collection.insert_one(document)

        return jsonify({'result': filtered_text.split('\n')})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
