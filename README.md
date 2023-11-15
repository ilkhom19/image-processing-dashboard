# Image Processing Dashboard Documentation

## Introduction
The Image Processing Dashboard is a web application built using Streamlit and Python. It allows users to upload images and apply various image processing filters and operations to explore different visual effects.

## Features
- **Filter Options:** Choose from a variety of image processing filters and operations.
- **Real-time Preview:** View the original and filtered images side by side.
- **User-Friendly Interface:** Simple and intuitive design for easy navigation.

Filter Options

Original: Display the original uploaded image.

Grayscale: Convert the image to grayscale.

Image Negative: Apply the negative of the image.

Scalar Multiplication: Adjust image brightness through scalar multiplication.

Power Law: Apply a power-law transformation to the image.

Log Transformation: Apply a logarithmic transformation to the image.

Min-Max Stretching: Perform min-max stretching for contrast enhancement.

Histogram Equalization: Enhance image contrast using histogram equalization.

Mean Filter: Apply a mean filter to the image.

Median Filter: Apply a median filter to the image.

Max Filter: Apply a max filter to the image.

Min Filter: Apply a min filter to the image.

Laplacian Filter: Apply a Laplacian filter to highlight edges.

Bilinear Interpolation: Resize the image using bilinear interpolation.

Nearest Neighbor Interpolation: Resize the image using nearest neighbor interpolation.

Region Growing Segmentation:



## Getting Started
1. Ensure you have Python installed on your machine.
2. Install required dependencies by running:
   ```bash
   pip install streamlit Pillow numpy scikit-image
