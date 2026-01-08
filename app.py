import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Page configuration
st.set_page_config(
    page_title="YOLO Pose Estimation",
    page_icon="🧍",
    layout="centered"
)

# App title
st.title("🧍 YOLO Human Pose Estimation")
st.markdown(
    "Upload an image to detect **human body keypoints and skeleton** "
    "using the YOLO Pose Estimation model."
)

# Load YOLO Pose model (cached for performance)
@st.cache_resource
def load_model():
    return YOLO("yolo11n-pose.pt")

model = load_model()

# File uploader
uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file).convert("RGB")
    st.subheader("📷 Original Image")
    st.image(image, use_container_width=True)

    # Convert image to numpy array
    img_array = np.array(image)

    # Run pose estimation
    with st.spinner("Analyzing human pose..."):
        results = model(img_array)

    # Display results
    st.subheader("🦴 Pose Estimation Result")
    result_image = results[0].plot()
    st.image(result_image, use_container_width=True)

    st.success("Pose detection completed successfully!")
else:
    st.info("Please upload an image to start pose detection.")
