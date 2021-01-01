import cv2 as cv
import numpy as np



def nothing(x):
    pass




cv.namedWindow('canny')
cv.createTrackbar('minThresh', 'canny', 50, 255, nothing)
cv.createTrackbar('maxThresh', 'canny', 150, 255, nothing)
cv.createTrackbar('cannyThresh', 'canny', 193, 255, nothing)


while True :

    img = cv.imread('sudoku.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    minThresh = cv.getTrackbarPos('minThresh', 'canny')
    maxThresh = cv.getTrackbarPos('maxThresh', 'canny')
    cannyThresh = cv.getTrackbarPos('cannyThresh', 'canny')

    edges = cv.Canny(gray, minThresh, maxThresh, apertureSize=3)
    lines = cv.HoughLines(edges, 1, np.pi/180, cannyThresh)



    for line in lines :

        rho, theta = line[0]

        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv.imshow('houghLines', img)
    cv.imshow('canny', edges)

    key = cv.waitKey(1) & 0xFF
    if key == 27 :
        break


cv.destroyAllWindows()