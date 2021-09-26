import cv2

image_path = ["1.jpg","11.jpg","1312.png", "GF-aG-ID4ss.jpg"]
while True:
    for i in image_path:
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        image = cv2.imread(i)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor= 1.1,
            minNeighbors= 2,
            minSize=(10, 10)
        )

        faces_detected = "Лиц обнаружено: " + format(len(faces))
        print(faces_detected)
        # Рисуем квадраты вокруг лиц
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 100), 2)
        def viewImage(image, name_of_window):
            cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
            cv2.imshow(name_of_window, image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        cv2.imwrite(f"{i}opencv.jpg", image)