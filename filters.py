from PIL import Image, ImageFilter, ImageOps, ImageEnhance, ImageMath
import numpy as np
from skimage import exposure


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
