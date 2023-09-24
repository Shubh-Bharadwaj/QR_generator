import pyqrcode, png
from pyqrcode import QRCode
print("Hello User!")
print("This program helps you to generate QR code for any given URL.")
print("="*40)
s = input("Enter URL to generate the QR Code: ")
print("="*40)
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)
url.png('myqr.png', scale = 6)
