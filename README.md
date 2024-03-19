
# OCR Web App Using Gradio and PyTesseract

This project is a locally run web application designed to extract text from images and PDF files through Optical Character Recognition (OCR) using PyTesseract, with a user-friendly interface powered by Gradio. The application supports various image formats such as JPG, JPEG, PNG, TIFF, and BMP, along with PDF documents.

## Features

- **Extract Text from Images and PDFs**: Perform OCR on various file formats to extract text.
- **Gradio Interface**: Provides a simple drag-and-drop interface for users to upload files and receive OCR results.
- **Local File Handling**: Saves uploads and OCR results locally for easy access and review.
- **Support for Multiple File Formats**: Handles PDF, JPG, JPEG, PNG, TIFF, and BMP files.

## Requirements

Before running the application, ensure you have the following installed:
- Python 3.6 or higher
- Gradio
- PyTesseract
- Pillow (PIL)
- NumPy
- PyMuPDF (fitz)
- pdf2image

You can install these dependencies using the following command:

```bash
pip install gradio pytesseract Pillow numpy PyMuPDF pdf2image
```
or
```bash
pip install -r requirements.txt
```

## Setup

1. **Clone the Repository**: First, clone this repository to your local machine.

2. **Install Dependencies**: Install the required Python libraries mentioned above.

3. **Run the Application**: Navigate to the project directory and run the following command:

    ```bash
    python app.py
    ```

This will start a local server and open the Gradio web interface in your default web browser. From there, you can upload image or PDF files to extract text.

## How It Works

Upon uploading a file through the Gradio interface, the application:

1. Determines the file type (image or PDF).
2. Performs OCR on the file using PyTesseract:
    - For images, it directly processes the file.
    - For PDFs, it converts each page to an image before performing OCR.
3. Saves the extracted text to a local file and displays the text in the Gradio interface.

## Limitations

- **PDF Conversion**: The application converts PDF pages to images for OCR, which may result in a loss of formatting and quality in the extracted text.
- **Language Support**: By default, OCR is optimized for English. For extracting text in other languages, additional configuration of PyTesseract may be required.

## Contributing

Contributions are welcome! If you have improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## License

This project is open-source and available under the GPL-3.0 License.
