import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')


def process(image) :
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.02, minNeighbors=2, minSize=(250, 250))

    for (x, y, width, height) in faces :
        cv.rectangle(image, (x, y), (x+width, y+height), (0, 255, 0), 3, cv.LINE_8)
        cv.putText(image, 'face', (x-20, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)

        roi_face_gray = image[y:y+height, x:x+width]
        roi_face_color = image[y:y+height, x:x+width]
        faces = eye_cascade.detectMultiScale(roi_face_gray)

        for (ex, ey, ew, eh) in faces :
            cv.rectangle(roi_face_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3, cv.LINE_8)
            cv.putText(roi_face_color, 'eye', (ex - 20, ey - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)

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