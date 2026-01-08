import cv2
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(page_title="YOLO Pose Estimation", layout="centered")
st.title("🧍 YOLO Human Pose Estimation")

@st.cache_resource
def load_model():
    return YOLO("yolo11n-pose.pt")  # auto-download

model = load_model()

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Original Image", use_container_width=True)

    img = np.array(image)

    with st.spinner("Detecting pose..."):
        results = model(img)

    st.image(results[0].plot(), caption="Pose Estimation Result", use_container_width=True)
