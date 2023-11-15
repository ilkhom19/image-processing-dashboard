import streamlit as st
from PIL import Image
from filters import *


def main():
    st.title("Image Processing Dashboard")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    col1, col2 = st.columns(2)

    if uploaded_image is not None:
        filter_option = st.selectbox("Select a Filter", get_filter_options())
        col1.image(uploaded_image, caption="Original", use_column_width=True, width=300)
        pil_image = Image.open(uploaded_image)
        filtered_image = apply_filter(pil_image, filter_option)
        col2.image(filtered_image, caption="Filtered", use_column_width=True, width=300)


def get_filter_options():
    return [
        "Original",
        "Grayscale",
        "Image Negative",
        "Scalar Multiplication",
        "Power Law",
        "Log Transformation",
        "Min-Max Stretching",
        "Histogram Equalization",
        "Mean Filter",
        "Median Filter",
        "Max Filter",
        "Min Filter",
        "Laplacian Filter",
        "Bilinear Interpolation",
        "Nearest Neighbor Interpolation"
    ]


def apply_filter(image, filter_option):
    if filter_option == "Grayscale":
        return convert_to_grayscale(image)
    elif filter_option == "Image Negative":
        return apply_image_negative(image)
    elif filter_option == "Scalar Multiplication":
        return apply_scalar_multiplication(image, 2.0)
    elif filter_option == "Power Law":
        return apply_power_law(image, gamma=1.5)
    elif filter_option == "Log Transformation":
        return apply_log_transformation(image)
    elif filter_option == "Min-Max Stretching":
        return apply_min_max_stretching(image)
    elif filter_option == "Histogram Equalization":
        return apply_histogram_equalization(image)
    elif filter_option == "Mean Filter":
        return apply_mean_filter(image)
    elif filter_option == "Median Filter":
        return apply_median_filter(image)
    elif filter_option == "Max Filter":
        return apply_max_filter(image)
    elif filter_option == "Min Filter":
        return apply_min_filter(image)
    elif filter_option == "Laplacian Filter":
        return apply_laplacian_filter(image)
    elif filter_option == "Bilinear Interpolation":
        return apply_bilinear_interpolation(image, scale_factor=2)
    elif filter_option == "Nearest Neighbor Interpolation":
        return apply_nearest_neighbor_interpolation(image, scale_factor=2)
    else:
        return image


if __name__ == "__main__":
    main()
