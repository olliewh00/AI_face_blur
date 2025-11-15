import cv2
import sys 

face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)

if face_cascade.empty():
    print("Error loading face cascade classifier.")
    print("Please ensure that OpenCV is correctly installed and the haarcascade files are accessible.")
    sys.exit(1)


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening video capture.")
    sys.exit(1)

while True:
    ret,frame = cap.read()

    if not ret:
        print("Error reading frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:

        face_roi = frame[y:y+h, x:x+w]
        blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)
        frame[y:y+h, x:x+w] = blurred_face

    cv2.imshow('Real-Time Face Blur', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 