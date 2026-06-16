import streamlit as st
from ultralytics import YOLO
import tempfile
from PIL import Image

st.set_page_config(page_title="YOLO目标检测", layout="wide")
st.title("🚀 YOLOv8 目标检测演示")

uploaded_file = st.file_uploader("上传一张图片", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as f:
        f.write(uploaded_file.getbuffer())
        temp_path = f.name

    @st.cache_resource
    def load_model():
        return YOLO('yolov8n.pt')

    model = load_model()
    results = model(temp_path)
    annotated = results[0].plot()
    st.image(annotated, caption="检测结果", use_column_width=True)