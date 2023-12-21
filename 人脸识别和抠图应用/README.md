
# 人脸识别和抠图应用

这是一个简单的人脸识别和抠图应用，使用前端（HTML + JavaScript）与后端（Python + Flask）。

## 前端

### 如何使用

1. 在浏览器中打开 `http://127.0.0.1:5000/index.html`。
2. 单击 "上传图片" 按钮，选择包含人脸的图片。
3. 上传成功后，会显示抠图后的人脸图像。

## 后端

### 安装依赖

确保你已经安装了 Flask 和 Pillow：

```bash
pip install Flask Pillow
```

并安装 OpenCV：

```bash
pip install opencv-python
```

### 如何运行

1. 打开终端，进入项目目录。
2. 运行后端 Flask 应用：

    ```bash
    python app.py
    ```

3. 在浏览器中打开 `http://127.0.0.1:5000/index.html`。

### 注意事项

- 上传的图片应为支持的格式（png、jpg、jpeg、gif）。
- 建议使用包含人脸的图片进行测试。

### 文件结构

- `app.py`: Flask 后端代码。
- `uploads/`: 存储上传的图片和抠图后的人脸图像。
- `index.html`: 前端页面。

### 后端处理流程

1. 接收前端上传的图片文件。
2. 使用 OpenCV 进行人脸检测。
3. 如果检测到人脸，抠图并保存为唯一的文件。
4. 返回抠图后的人脸图像的URL给前端。
