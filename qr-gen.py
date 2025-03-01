import qrcode

# Replace this with your link
url = "https://your-link-here.com"

# Create a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Generate the image
img = qr.make_image(fill="black", back_color="white")

# Save the QR code
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")

