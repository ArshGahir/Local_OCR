import gradio as gr
from PIL import Image
import pytesseract


def perform_ocr(image):
    # Extract text from Input Image
    # Convert to PIL from NP Array
    image = Image.fromarray(image)
    # Convert the input image to text
    text = pytesseract.image_to_string(image)
    return text

# Define the Gradio interface
iface = gr.Interface(fn=perform_ocr,
                     inputs=gr.Image(type="pil", label="Upload Image"),  # Use type="pil" for additional image format support
                     outputs=gr.Textbox(label="Extracted Text"),
                     title="OCR using Tesseract and Gradio",
                     description="Drag and Drop an Image or Click to Upload")


# Launch the Gradio app
if __name__ == "__main__":
    iface.launch()
