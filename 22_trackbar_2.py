# deneme 21 --version (2/3)

import cv2 as cv
import numpy as np

def nothing(x) :
    print(x)

img = np.zeros((512,512,3), np.uint8)

cv.namedWindow('pencere')

cv.createTrackbar('B', 'pencere', 0, 255, nothing)
cv.createTrackbar('G', 'pencere', 0, 255, nothing)
cv.createTrackbar('R', 'pencere', 0, 255, nothing)
cv.createTrackbar('ON / OF', 'pencere', 0, 1 ,nothing)

while True :
    b = cv.getTrackbarPos('B', 'pencere')
    g = cv.getTrackbarPos('G', 'pencere')
    r = cv.getTrackbarPos('R', 'pencere')
    switch = cv.getTrackbarPos('ON / OF', 'pencere')

    if switch :
        img[:] = [b, g, r]

    cv.imshow('pencere', img)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q') :
        break

cv.destroyAllWindows()