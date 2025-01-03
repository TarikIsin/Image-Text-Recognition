from PIL import Image, ImageFilter
import pytesseract
import cv2
import numpy as np
import os

# Specify the correct path for Tesseract (for Windows)
tesseract_path = os.getenv('TESSERACT_PATH')

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    print("Tesseract path not found in the environment variable.")

# Open the image
img_path = "images\yazi.jpg"
img = Image.open(img_path)

# Step 1: Grayscale (convert the image to grayscale)
img_gray = img.convert('L')

# Step 2: Binarization (convert the image to black and white)
# If using OpenCV, the following binarization process can be done:
img_gray_np = np.array(img_gray)
_, img_binary = cv2.threshold(img_gray_np, 150, 255, cv2.THRESH_BINARY)

# Step 3: Sharpening the image
img_sharpened = img_gray.filter(ImageFilter.SHARPEN)

# Step 5: OCR to recognize text
text = pytesseract.image_to_string(img_sharpened)

# Print the recognized text
print(text)
