# PDF to Text Converter

This project provides a script to convert PDF documents into text files using Python. It leverages libraries like `pytesseract` for Optical Character Recognition (OCR) and `pdf2image` to convert PDF pages into images for processing.

## Features

- Converts PDF pages to images.
- Extracts text from images using OCR.
- Supports multiple languages for text extraction.
- Saves the extracted text into a text file.

## Requirements

- Python 3.6+
- Tesseract-OCR
- Poppler

## Installation

### Python Libraries

Install the required Python libraries using pip:

```sh
pip install pytesseract pdf2image pillow
```

### Tesseract-OCR

- **Windows**: Download and install Tesseract-OCR from [here](https://github.com/UB-Mannheim/tesseract/wiki).
- **Linux**: Install Tesseract-OCR using your package manager.

  ```sh
  sudo apt-get install tesseract-ocr
  ```

### Poppler

- **Windows**: Download Poppler for Windows from [here](http://blog.alivate.com.au/poppler-windows/) and add the bin folder to your PATH.
- **Linux**: Install Poppler using your package manager.

  ```sh
  sudo apt-get install poppler-utils
  ```

## Usage

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/pdf-to-text-converter.git
    cd pdf-to-text-converter
    ```

2. Update the environment PATH to include Python and Poppler:

    ```python
    import os
    os.environ["PATH"] += os.pathsep + os.pathsep.join(["Python310"])
    ```

3. Run the script:

    ```sh
    python convert_pdf_to_text.py
    ```

4. Follow the prompts to enter the PDF path and the language of the document.

## Script Details

### Environment Setup

The script starts by updating the PATH environment variable to include the paths for Python and other dependencies. It also sets the Tesseract command if the script is running on Windows.

### Input and Output

- **Input**: The script prompts the user to input the path to the PDF file and the language of the PDF.
- **Output**: The extracted text is saved in a file named `datex.txt` in the specified output directory.

### Main Function

- Converts PDF pages to images.
- Performs OCR on each image to extract text.
- Writes the extracted text to a file.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)
- [Poppler](https://poppler.freedesktop.org/)
- [pdf2image](https://github.com/Belval/pdf2image)
- [Pillow](https://python-pillow.org/)

---

