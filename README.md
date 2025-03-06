# PDF Compressor

## Overview
This is a Python-based wrapper script that compresses PDF files using **Ghostscript**. It allows users to select a PDF file and compress it at different quality levels.

## Features
- Compress PDF files to reduce file size.
- Supports multiple compression levels:
  - **0:** Default (72 dpi images)
  - **1:** Prepress (high-quality, 300 dpi images)
  - **2:** Printer (high-quality, 300 dpi images)
  - **3:** eBook (low-quality, 150 dpi images)
  - **4:** Screen (screen-view only, 72 dpi images)
- Backup option to store the original file.
- Opens the compressed file after processing.

## Installation

### Prerequisites
- Python 3.x
- **Ghostscript** installed and added to system PATH

### Setup
1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd PDF-Compressor
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage
### Command Line Usage
Run the script in the terminal:
```sh
python app.py -c 2 --backup --open
```
Options:
- `-c` or `--compress`: Set compression level (0 to 4)
- `-b` or `--backup`: Backup the original PDF before compression
- `--open`: Open the compressed PDF after completion

### GUI Usage
1. Run the script without arguments:
   ```sh
   python app.py
   ```
2. A file dialog will open. Select a **PDF file**.
3. The compressed PDF will be saved to the **Desktop** as `compressed.pdf`.

## Example
To compress a PDF with **prepress quality** and keep a backup:
```sh
python app.py -c 1 -b
```

## Future Enhancements
- Add support for batch processing multiple PDFs.
- Provide a graphical user interface for compression options.
