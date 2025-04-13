# Clipboard OCR Paster

This tool grabs an image from your clipboard (e.g. a screenshot), extracts the text using Tesseract OCR, copies it to your clipboard, and pastes it automatically. Triggered by `Ctrl+Shift+V`.

## Features

- OCR directly from clipboard images  
- Auto-copies and pastes the extracted text  
- Cross-platform Tesseract path setup  
- Quick hotkey: `Ctrl+Shift+V`  
- Exit anytime with `Shift+Esc`

## Requirements

- Python 3.7+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed (Windows default path is used if not configured)

## Installation

Clone the repository and install dependencies using the `requirements.txt` file:

```bash
git clone https://github.com/sumdeusvitae/clipboardPaster.git
cd clipboardPaster
pip install -r requirements.txt
```

Install Tesseract separately and make sure it's accessible from your system.

## Usage

```bash
python main.py
```

Then use `Ctrl+Shift+V` to run OCR on any image in your clipboard.

Press `Shift+Esc` to stop the script.

## Notes

- The script sets the `TESSERACT_PATH` environment variable automatically on first run.
- Windows users: make sure Tesseract is installed to the default path (`C:\Program Files\Tesseract-OCR\tesseract.exe`) or set it manually.
- macOS/Linux: The path will be appended to your shell config (`.bashrc` or `.zshrc`).

## Dependencies

- pytesseract  
- pillow  
- pyperclip  
- keyboard
