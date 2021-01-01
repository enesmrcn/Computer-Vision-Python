import cv2 as cv
import numpy as np


def skip(x) :
    pass

cv.namedWindow('parameters')
cv.namedWindow('panel')


cv.createTrackbar('minThresh', 'parameters', 50, 255, skip)
cv.createTrackbar('maxThresh', 'parameters', 150, 255, skip)
cv.createTrackbar('houghThresh', 'parameters', 100, 255, skip)
cv.createTrackbar('linesNumb', 'parameters', 100, 255, skip)
cv.createTrackbar('minLenght', 'parameters', 100, 255, skip)
cv.createTrackbar('maxGap', 'parameters', 10, 50, skip)
cv.createTrackbar('reset', 'parameters', 0, 1, skip)

reset = 0

while True :

    img = cv.imread('sudoku.png')
    panel = np.ones((350, 500, 3), np.uint8)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    if reset == 0 :
        minThresh = cv.getTrackbarPos('minThresh', 'parameters')
        maxThresh = cv.getTrackbarPos('maxThresh', 'parameters')
        houghThresh = cv.getTrackbarPos('houghThresh', 'parameters')
        linesNumb = cv.getTrackbarPos('linesNumb', 'parameters')
        minLenght = cv.getTrackbarPos('minLenght', 'parameters')
        maxGap = cv.getTrackbarPos('maxGap', 'parameters')
        cv.rectangle(panel, (0, 300), (500, 350), (0, 0, 255), -1)
    else :
        minThresh = 50
        maxThresh = 150
        houghThresh = 100
        linesNumb = 100
        minLenght = 100
        maxGap = 10
        cv.rectangle(panel, (0, 300), (500, 350), (255, 0, 0), -1)
        print('1')

    reset = cv.getTrackbarPos('reset', 'parameters')

    canny = cv.Canny(gray, minThresh, maxThresh, apertureSize=3)
    lines = cv.HoughLinesP(canny, 1, np.pi/180, houghThresh, lines=linesNumb, minLineLength=minLenght, maxLineGap=maxGap)

    for line in lines :
        x1, y1, x2, y2 = line[0]
        #print(line[0],'\n')
        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2, cv.LINE_AA)

    #for line in lines :            # alternatif olarak bu sekilde de loop acabilirsin
    #    for x1, y1, x2, y2 in line :
    #        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2, cv.LINE_AA)


    #draw()
    cv.rectangle(panel, (0, 0), (int(1.96*minThresh), 50), (0, 255, 0), -1)
    cv.rectangle(panel, (0, 50), (int(1.96*maxThresh), 100), (255, 0, 0), -1)
    cv.rectangle(panel, (0, 100), (int(1.96*houghThresh), 150), (0, 0, 255), -1)
    cv.rectangle(panel, (0, 150), (int(1.96*linesNumb), 200), (255, 255, 0), -1)
    cv.rectangle(panel, (0, 200), (int(1.96*minLenght), 250), (255, 0, 255), -1)
    cv.rectangle(panel, (0, 250), (50*maxGap, 300), (0, 255, 255), -1)



    cv.imshow('panel', panel)
    cv.imshow('probabilistic', img)
    cv.imshow('parameters', canny)

    key = cv.waitKey(40) & 0xFF
    if key == 27 :
        break

cv.destroyAllWindows()