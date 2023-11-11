import streamlit as st
from PIL import Image, ImageFilter

def main():
    st.title("Image Filter App")

    # Upload image through Streamlit
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        # Add a filter selection dropdown
        filter_option = st.selectbox("Select a Filter", ["Original", "Blur", "Sharpen", "Edge Enhancement"])

        # Process and display the filtered image
        if filter_option == "Blur":
            filtered_image = apply_blur(uploaded_image)
        elif filter_option == "Sharpen":
            filtered_image = apply_sharpen(uploaded_image)
        elif filter_option == "Edge Enhancement":
            filtered_image = apply_edge_enhancement(uploaded_image)
        else:
            filtered_image = Image.open(uploaded_image)

        st.image(filtered_image, caption="Filtered Image", use_column_width=True)

def apply_blur(image):
    return image.filter(ImageFilter.BLUR)

def apply_sharpen(image):
    return image.filter(ImageFilter.SHARPEN)

def apply_edge_enhancement(image):
    return image.filter(ImageFilter.EDGE_ENHANCE)

if __name__ == "__main__":
    main()
