import streamlit as st
from PIL import Image, ImageFilter, ImageOps, ImageEnhance, ImageMath
import numpy as np
from skimage import exposure


def main():
    st.title("Image Processing Dashboard")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Original", use_column_width=True, width=300)
        pil_image = Image.open(uploaded_image)

        filter_option = st.selectbox("Select a Filter", get_filter_options())

        filtered_image = apply_filter(pil_image, filter_option)
        st.image(filtered_image, caption="Filtered", use_column_width=True, width=300)


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
        "Nearest Neighbor Interpolation",
        "Region Growing Segmentation",
        "Run Length Encoding",
        "Huffman Encoding",
        "Arithmetic Encoding"
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
    elif filter_option == "Region Growing Segmentation":
        return apply_region_growing_segmentation(image)
    elif filter_option == "Run Length Encoding":
        return apply_run_length_encoding(image)
    elif filter_option == "Huffman Encoding":
        return apply_huffman_encoding(image)
    elif filter_option == "Arithmetic Encoding":
        return apply_arithmetic_encoding(image)
    else:
        return image


def convert_to_grayscale(image):
    return ImageOps.grayscale(image)


def apply_image_negative(image):
    return ImageOps.invert(image)


def apply_scalar_multiplication(image, scalar):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(scalar)


def apply_power_law(image, gamma):
    img_array = np.array(image)

    img_transformed = np.power(img_array / 255.0, gamma) * 255.0

    return Image.fromarray(img_transformed.astype(np.uint8))


def apply_log_transformation(image):
    img_array = np.array(image)

    # small constant to avoid log(0)
    img_array_log = np.log1p(img_array)

    # Rescale the values to the 0-255 range
    img_array_log = (img_array_log / img_array_log.max()) * 255

    return Image.fromarray(img_array_log.astype(np.uint8))


def apply_min_max_stretching(image):
    return ImageOps.autocontrast(image)


def apply_histogram_equalization(image):
    img_array = np.array(image)

    img_array = img_array.astype(np.float64)
    img_eq = exposure.equalize_hist(img_array)

    return Image.fromarray((img_eq * 255).astype(np.uint8))


def apply_mean_filter(image):
    return image.filter(ImageFilter.Kernel((3, 3), [1, 1, 1, 1, 1, 1, 1, 1, 1], scale=9))


def apply_median_filter(image):
    return image.filter(ImageFilter.MedianFilter(size=3))


def apply_max_filter(image):
    return image.filter(ImageFilter.MaxFilter(size=3))


def apply_min_filter(image):
    return image.filter(ImageFilter.MinFilter(size=3))


def apply_laplacian_filter(image):
    # Laplacian filter kernel
    laplacian_kernel = ImageFilter.Kernel((3, 3), [-1, -1, -1, -1, 8, -1, -1, -1, -1], scale=1)
    return image.filter(laplacian_kernel)


def apply_bilinear_interpolation(image, scale_factor):
    width, height = image.size
    new_size = (width * scale_factor, height * scale_factor)
    return image.resize(new_size, resample=Image.BILINEAR)


def apply_nearest_neighbor_interpolation(image, scale_factor):
    width, height = image.size
    new_size = (width * scale_factor, height * scale_factor)
    return image.resize(new_size, resample=Image.NEAREST)


def apply_region_growing_segmentation(image):

    return "implement me!"


def apply_run_length_encoding(image):

    return "implement me!"


def apply_huffman_encoding(image):

    return "implement me!"


def apply_arithmetic_encoding(image):

    return "implement me!"


if __name__ == "__main__":
    main()
