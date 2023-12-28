import pyqrcode
from pyqrcode import QRCode

s = input("Insert your link : ")
qr = pyqrcode.create(s)

qr.png("qrcode.png", scale=8)
