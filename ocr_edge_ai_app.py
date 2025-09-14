import streamlit as st
import easyocr
import numpy as np
import cv2
from PIL import Image

st.set_page_config(page_title="Edge AI OCR App", layout="centered")

st.title("📄 OCR Edge AI Demo (Runs Offline)")
st.markdown("Upload an image and extract text using EasyOCR (runs fully on your laptop).")

# Initialize OCR Reader
@st.cache_resource
def load_reader():
    return easyocr.Reader(['en'])  # You can add more languages if needed

reader = load_reader()

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert PIL image to OpenCV format
    img_np = np.array(image)
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    with st.spinner("Running OCR..."):
        results = reader.readtext(img_bgr)

    st.success("OCR Completed!")

    # Show extracted text
    st.subheader("📝 Extracted Text:")
    for bbox, text, conf in results:
        st.markdown(f"- `{text}` (Confidence: {conf:.2f})")

    # Draw boxes and labels
    for bbox, text, conf in results:
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))
        cv2.rectangle(img_bgr, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(img_bgr, text, (top_left[0], top_left[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Convert back to RGB for display
    annotated_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    st.subheader("🔍 Annotated Image with OCR Results")
    st.image(annotated_img, use_column_width=True)

else:
    st.info("Please upload an image to begin.")
