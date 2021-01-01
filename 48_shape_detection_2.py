#basit shape detection
# kare ile dikdortgeni ayirt eder

import  cv2 as cv

img = cv.imread('shapes2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

__, thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)

contours, __ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours :
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    cv.drawContours(img, [approx], 0, (0, 0, 0), 3, cv.LINE_4)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3 :
        cv.putText(img, 'triangle', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    elif len(approx) == 4 :
        (x1, y1, width, height) = cv.boundingRect(contour)
        ratio = float(width/height)
        if ratio > 0.95 and ratio < 1.1 :
            cv.putText(img, 'square', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        else  :
            cv.putText(img, 'reqtangle', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    elif len(approx) == 5 :
        cv.putText(img, 'pentagon', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    elif len(approx) == 5 :
        cv.putText(img, 'pentagon', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    elif len(approx) == 6 :
        cv.putText(img, 'hexagon', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    elif len(approx) == 7 :
        cv.putText(img, 'octav', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    elif len(approx) == 10 :
        cv.putText(img, 'star', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    else :
        cv.putText(img, 'circle', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cv.imshow('shape_detection', img)
cv.waitKey(0)
cv.destroyAllWindows()