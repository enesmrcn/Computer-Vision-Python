import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalcatface_extended.xml')

image = cv.imread('enes.png')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.02, minNeighbors=2, minSize=(200, 200))

for (x, y, width, height) in faces :
    cv.rectangle(image, (x, y), (x+width, y+height), (0, 255, 0), 3, cv.LINE_8)

cv.imshow('at', image)
cv.waitKey(0)
cv.destroyAllWindows()