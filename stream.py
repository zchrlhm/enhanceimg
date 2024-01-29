import streamlit as st
from PIL import Image, ImageEnhance

def enhance_image(image, enhancement_factor):
    enhancer = ImageEnhance.Brightness(image)
    enhanced_image = enhancer.enhance(enhancement_factor)
    return enhanced_image

def main():
    st.title("Enhance Your Images")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        enhancement_factor = st.slider("Enhancement Factor", min_value=0.0, max_value=2.0, value=1.0, step=0.01)

        if st.button("Enhance"):
            image = Image.open(uploaded_file)
            enhanced_image = enhance_image(image, enhancement_factor)
            st.image(enhanced_image, caption="Enhanced Image", use_column_width=True)

if __name__ == "__main__":
    main()