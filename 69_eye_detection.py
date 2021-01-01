import cv2 as cv


face_cascade = cv.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')

image = cv.imread('enes.png')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.02, minNeighbors=2, minSize=(200, 200))


for (x, y, width, height) in faces :

    cv.rectangle(image, (x, y), (x+width, y+height), (0, 255, 0), 3, cv.LINE_8)
    cv.putText(image, 'face', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    roi_eye_gray = gray[y:y+height, x:x+width]
    roi_eye_color = image[y:y+height, x:x+width]
    eyes = eye_cascade.detectMultiScale(roi_eye_gray)

    for (ex, ey, ew, eh) in eyes :
        cv.rectangle(roi_eye_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 4, cv.LINE_8)
        cv.putText(roi_eye_color, 'eye', (ex, ey - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


cv.imshow('face_detection', image)

cv.waitKey(0)
cv.destroyAllWindows()