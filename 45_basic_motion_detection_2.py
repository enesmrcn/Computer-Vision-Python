import cv2 as cv
import numpy as np

cap = cv.VideoCapture('vtest.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened() :
    diff = cv.absdiff(frame1, frame2)

    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0 )
    __, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)

    contours, __ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    #cv.drawContours(frame1, contours, -1, (0, 0, 255), 2, cv.LINE_AA)
    
    
    for contour in contours :
        (x, y, width, height) = cv.boundingRect(contour)
        
        if cv.contourArea(contour) < 700 :
            continue
            
        cv.rectangle(frame1, (x, y), (x+width, y+height), (0, 255, 0), 2, cv.LINE_AA)
        cv.putText(frame1, "Status : {}".format('Motion Detected'), (30, 30), cv.FONT_HERSHEY_SIMPLEX,
                   1, (0, 0, 255), 3)

    cv.imshow('motion_detection', frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    key = cv.waitKey(40) & 0xFF
    if key == ord('q') :
        break

cap.release()
cv.destroyAllWindows()