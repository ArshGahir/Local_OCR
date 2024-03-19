import gradio as gr
from PIL import Image
import pytesseract
import numpy as np
import fitz
from pdf2image import convert_from_path
import uuid
import os
import shutil

# Upload File Save Location

# local
save_path = "uploads/"

# Google Cloud Bucket


# AWS S3


# Azure Blob Storage



# General OCR Function

def perform_ocr(image):
    # Extract text from Input Image
    # Convert to PIL from NP Array
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)

    # Convert the input image to text
    text = pytesseract.image_to_string(image)
    return text


# Save Extracted Text to a File

def save_text(text, file_path):
    with open(file_path, "w") as file:
        file.write(text)
    return file_path


# Determine Input File Type

def determine_input_type(input_file_path):
    if input_file_path.endswith(".pdf"):
        return "pdf"
    elif input_file_path.endswith((".jpg", ".jpeg", ".png", ".tiff", ".bmp")):
        return "image"
    else:
        return "Invalid Input Type"


# OCR function for PDFs

def ocr_pdf(pdf_path):

    results = []
    # Method 1: convert pdfs to images and then perform OCR
    try:
        # Convert PDF pages to Images
        images = convert_from_path(pdf_path)

        # Perform OCR on each page
        for image in images:
            results.append(perform_ocr(image))

        return " ".join(results)
    
    # Method 2: retain pdf format and perform OCR
    except Exception as e:
        print(f"Error in Processing PDF: {e}")
        print(f"Trying alternative...")
        try:
            pages = fitz.open(pdf_path)
            for page in pages:
                text = page.get_text()
                results.append(text)

            return " ".join(results)
        except Exception as e:
            return f"Error in Processing PDF: {e}"
    
# OCR function for images

def ocr_image(image):
    return perform_ocr(image)

# Route the request to the appropriate OCR function

def route_request(input_type, input_file):
    if input_type == "pdf":
        return ocr_pdf(input_file)
    elif input_type == "image":
        return ocr_image(input_file)
    else:
        return "Invalid Input Type"
    
# Process Uploaded File
def process_upload(file):
# Generate a unique identifier for this upload to prevent file name clashes
    # Extract file name and extension
    file_name, file_extension = os.path.splitext(file.name)

    # Create unique file names for the saved input and OCR result to avoid overwrites
    unique_id = str(uuid.uuid4())[:8]  # Generate a unique identifier
    saved_input_file_name = f"{file_name}_{unique_id}_{file_extension}"
    ocr_result_file_name = f"{file_name}_{unique_id}_ocr.txt"

    saved_input_path = os.path.join(save_path, saved_input_file_name)
    ocr_result_path = os.path.join(save_path, ocr_result_file_name)

    # Handle file based on its type
    if isinstance(file, str):  # If 'file' is a file path, copy it to the uploads folder
        shutil.copy(file, saved_input_path)
        input_file_path = file
    else:  # If 'file' is a file-like object, save it and use a temp file for processing
        with open(saved_input_path, 'wb') as f_out:
            f_out.write(file.read())
        # Use the saved file for processing
        input_file_path = saved_input_path

    # Perform OCR
    result_text = route_request(determine_input_type(saved_input_path), saved_input_path)

    # Save the OCR result
    with open(ocr_result_path, "w") as text_file:
        text_file.write(result_text)

    return input_file_path, ocr_result_path, result_text

# Define the Gradio interface
iface = gr.Interface(fn=process_upload,
                     inputs=gr.File(label="Upload Image of PDF"),
                     outputs=[gr.Textbox(label="Input File Path"), gr.Textbox(label="Output File Path"), gr.Textbox(label="Extracted Text")],
                     title="OCR using Tesseract and Gradio",
                     description="Drag and Drop an Image/PDF or Click to Upload",
                     flagging_callback=gr.SimpleCSVLogger())


# Launch the Gradio app
if __name__ == "__main__":
    iface.launch()
