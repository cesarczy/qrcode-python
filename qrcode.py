import pyqrcode
import png

qrcode = pyqrcode.create("https://www.linkedin.com/in/erlan-cesar-siqueira-da-silva/")

# Salvar o QR Code
qrcode.png("cesar-siqueira.png", scale=6)