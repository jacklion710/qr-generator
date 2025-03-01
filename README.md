# QR Code Generator

A simple script for generating QR codes and associating them with a URL.

## Installation

1. Ensure you have Python installed on your system

2. Install the required dependency:

```bash
pip install qrcode
```

or

```bash
pip install qrcode[pil]
```

## Usage

1. Clone this repository or download the script
2. Replace the URL string in `qr-gen.py` with your target URL:

```python
# Replace this with your link
url = "https://your-link-here.com"
```

3. Run the script to generate the QR code:

```bash
python qr-gen.py
```

The QR code will be generated and saved as `qrcode.png` in the same directory.

## Features

- Generates a QR code with standard error correction
- Creates a PNG image with black QR code on white background
- Default QR code settings:
  - Version 1
  - Error correction level: L (low)
  - Box size: 10 pixels
  - Border: 4 boxes

## Requirements

- Python 3.x
- qrcode library with PIL/Pillow support