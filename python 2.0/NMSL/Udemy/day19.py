# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from PIL import Image
 
st.subheader("Color to Grayscale Converter")
    
uploaded_image = st.file_uploader("Upload Image")

    
with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if uploaded_image:
    img2 = Image.open(uploaded_image)
    gray_camera_img2 = img2.convert('L')
    st.image(gray_camera_img2)
 
 
if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)
    