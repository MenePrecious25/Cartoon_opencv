import numpy as np
import streamlit as st
import cv2



def apply_cartoon_effect(image):
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(gray_image, (21, 21), 0)
    
    # Apply edge detection
    edges = cv2.Canny(blurred_image, threshold1=50, threshold2=100)
    
    # Apply thresholding
    thresh = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 5, 0.77)
    return thresh

def main():
    st.title('Cartoonify Your Image!')
    
    # Upload image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_image is not None:
        # Read image
        file_bytes = uploaded_image.getvalue()
        nparr = np.frombuffer(file_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Apply cartoon effect
        cartoon_image = apply_cartoon_effect(image)
        
        # Display original and cartoon images
        st.image([image, cartoon_image], caption=['Original Image', 'Cartoon Image'], width=300)

if __name__ == "__main__":
    main()
