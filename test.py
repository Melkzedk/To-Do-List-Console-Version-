import qrcode

data = input("Enter text or URL: ")
qr = qrcode.make(data)
qr.save("qrcode.png")
print("✅ QR Code saved as qrcode.png")
