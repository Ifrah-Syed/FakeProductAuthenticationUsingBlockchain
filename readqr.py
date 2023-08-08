
import cv2
file_path = "a.png" 
img=cv2.imread(file_path)
det=cv2.QRCodeDetector()
val, pts, st_code=det.detectAndDecode(img)
print(val)
