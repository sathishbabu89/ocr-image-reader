# ocr-image-reader
This App is a lightweight, offline-capable OCR application built with Streamlit and EasyOCR. It allows users to upload images and extract text using deep learning models, all running locally without cloud dependencies. Ideal for edge devices and privacy-sensitive environments.

---

## 📄 `README.md` Content

```markdown
# Edge AI OCR App

This is a Streamlit-based web application that performs Optical Character Recognition (OCR) using EasyOCR. The app runs entirely offline on your local machine and allows users to upload images and extract text from them using a deep learning-based OCR engine.

## 🚀 Features

- 📄 Upload images in JPG, JPEG, or PNG format
- 🔍 Extract text using EasyOCR (supports multiple languages)
- 🧠 Runs fully offline using Edge AI (no cloud dependency)
- 🖼️ Displays annotated image with bounding boxes and recognized text
- ⚡ Fast and lightweight interface using Streamlit

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/edge-ai-ocr-app.git
   cd edge-ai-ocr-app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Upload an image and view the extracted text and annotated image.

## 📦 Dependencies

- Streamlit
- EasyOCR
- NumPy
- OpenCV (headless)
- Pillow
- Torch

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
```
