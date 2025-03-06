"""
Simple python wrapper script to use Ghostscript function to compress PDF files.

Compression levels:
    0: default - almost identical to /screen, 72 dpi images
    1: prepress - high quality, color preserving, 300 dpi images
    2: printer - high quality, 300 dpi images
    3: ebook - low quality, 150 dpi images
    4: screen - screen-view-only quality, 72 dpi images

Dependency: Ghostscript.
Make sure Ghostscript is installed and its executable path is set in your environment.
"""

import argparse
import os.path
import shutil
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog

def compress(input_file_path, output_file_path, power=0, gs_executable="gs"):
    """Function to compress PDF via Ghostscript command line interface"""
    quality = {
        0: "/default",
        1: "/prepress",
        2: "/printer",
        3: "/ebook",
        4: "/screen"
    }

    # Basic controls
    # Check if valid path
    if not os.path.isfile(input_file_path):
        print("Error: invalid path for input PDF file.", input_file_path)
        sys.exit(1)

    # Check compression level
    if power < 0 or power > len(quality) - 1:
        print("Error: invalid compression level, run pdfc -h for options.", power)
        sys.exit(1)

    # Check if file is a PDF by extension
    if input_file_path.split('.')[-1].lower() != 'pdf':
        print(f"Error: input file is not a PDF.", input_file_path)
        sys.exit(1)

    gs = gs_executable
    print("Compress PDF...")
    initial_size = os.path.getsize(input_file_path)
    subprocess.call(
        [
            gs,
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS={}".format(quality[power]),
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            "-sOutputFile={}".format(output_file_path),
            input_file_path,
        ]
    )
    final_size = os.path.getsize(output_file_path)
    ratio = 1 - (final_size / initial_size)
    print("Compression by {0:.0%}.".format(ratio))
    print("Final file size is {0:.5f}MB".format(final_size / 1000000))
    print("Done.")

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-c", "--compress", type=int, help="Compression level from 0 to 4")
    parser.add_argument("-b", "--backup", action="store_true", help="Backup the old PDF file")
    parser.add_argument("--open", action="store_true", default=False, help="Open PDF after compression")
    args = parser.parse_args()

    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    # Ask for input PDF file
    input_file_path = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF files", "*.pdf")])
    if not input_file_path:
        print("No input file selected. Exiting.")
        return

    # Output file path on desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file_path = os.path.join(desktop_path, "compressed.pdf")

    # In case no compression level is specified, default is 2 '/ printer'
    if not args.compress:
        args.compress = 2

    # Run compression
    compress(input_file_path, output_file_path, power=args.compress)

    # Handle file operations
    if args.backup:
        shutil.copyfile(input_file_path, os.path.join(desktop_path, "backup.pdf"))
    if args.open:
        subprocess.call(["open", output_file_path])

if __name__ == "__main__":
    main()
