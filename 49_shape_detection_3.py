#basit shape detection
# kare ile dikdortgeni ayirt eder
#gercek zamanli video kayit uzerinde tespit yapar

import cv2 as cv

cap = cv.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened() :
    gray = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)

    __, thresh = cv.threshold(gray, 110, 255, cv.THRESH_BINARY)

    contours, __ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    for contour in contours:
        if cv.contourArea(contour) < 250:
            continue
        approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
        cv.drawContours(frame1, [approx], 0, (0), 3, cv.LINE_4)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        lenght = len(approx)
        if lenght == 3:
            cv.putText(frame1, 'triangle', (x, y - 15), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        elif lenght == 4:
            (x1, y1, width, height) = cv.boundingRect(contour)
            ratio = float(width / height)
            if ratio > 0.95 and ratio < 1.1:
                cv.putText(frame1, 'square', (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
            else:
                cv.putText(frame1, 'reqtangle', (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        elif lenght == 5:
            cv.putText(frame1, 'pentagon', (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        elif lenght == 5:
            cv.putText(frame1, 'pentagon', (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        elif lenght == 6:
            cv.putText(frame1, 'hexagon', (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        elif lenght == 7:
            cv.putText(frame1, 'octav', (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        elif lenght == 10:
            cv.putText(frame1, 'star', (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        elif 10 < lenght < 15 :
            cv.putText(frame1, 'circle', (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)


    cv.imshow('shape_detection', frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    key = cv.waitKey(40) & 0xFF
    if key == 27:
        break

cv.destroyAllWindows()
cap.release()