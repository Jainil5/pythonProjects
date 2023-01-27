import qrcode
 
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("a.pdf")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save("medium.png")


""" to read a qr
import cv2
img=cv2.imread("medium.png")
det=cv2.QRCodeDetector()
val, pts, st_code=det.detectAndDecode(img)
print(val)
Output:
https://abhijithchandradas.medium.com/
"""