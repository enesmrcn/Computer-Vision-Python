import cv2 as cv


cap = cv.VideoCapture('vtest.avi')
#cap = cv.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()


while cap.isOpened() :

    diff = cv.absdiff(frame1, frame2)

    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

    blur = cv.GaussianBlur(gray, (5, 5), 0)
    __, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)

    contours, __ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv.imshow('pencere', frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    key = cv.waitKey(40) & 0xFF
    if key == 27 :
        break


cv.destroyAllWindows()
cap.release()