import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalcatface_extended.xml')


def process(image) :
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.02, minNeighbors=2, minSize=(250, 250))

    for (x, y, width, height) in faces :
        cv.rectangle(image, (x, y), (x+width, y+height), (0, 255, 0), 3, cv.LINE_8)
        cv.putText(image, 'face', (x-20, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    return image


cap = cv.VideoCapture(0)

while cap.isOpened() :

    __, frame = cap.read()

    frame = process(frame)
    cv.imshow('face_detection', frame)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q') :
        break

cv.destroyAllWindows()