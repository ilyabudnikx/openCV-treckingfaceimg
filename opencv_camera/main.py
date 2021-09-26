import cv2

cap = cv2.VideoCapture(0)
cap.set(3,1280) # Установление длины окна
cap.set(4,700)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(3))
print(cap.get(4))