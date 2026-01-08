# app.py
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Page config
st.set_page_config(page_title="YOLO Pose Detection", layout="centered")

st.title("🕺 YOLO Pose Detection App")
st.write("Upload an image and the model will detect poses in it.")

# Load model (once)
@st.cache_resource
def load_model():
    return YOLO('yolo11n-pose.pt')

model = load_model()

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    st.write("Running pose detection... ⏳")
    
    # Run the model
    result = model(np.array(image))
    
    # Show result
    st.write("Pose detection result:")
    result[0].show()  # This opens in default image viewer (for debugging)
    
    # Convert result image to show in Streamlit
    annotated_image = result[0].plot()  # This returns a numpy array with annotations
    st.image(annotated_image, caption='Annotated Image', use_column_width=True)
