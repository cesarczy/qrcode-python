import pyqrcode
import png

qrcode = pyqrcode.create("https://www.linkedin.com/in/erlan-cesar-siqueira-da-silva/")

# Save the QR CODE
qrcode.png("cesar-siqueira.png", scale=6)
