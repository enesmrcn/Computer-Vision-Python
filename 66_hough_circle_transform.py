import cv2 as cv
import numpy as np


image = cv.imread('smarties.png')
copy_img = image.copy()

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blur = cv.medianBlur(gray, 5)
circles = cv.HoughCircles(image=blur, method=cv.HOUGH_GRADIENT, dp=1, minDist=20, param1=50,
                          param2=30,
                          minRadius=0,
                          maxRadius=50)

detected_circles = np.uint16(np.around(circles))

for (x, y, r) in detected_circles[0, :] :
    cv.circle(image, (x, y), r, (0, 255, 255), 2, cv.LINE_AA)

cv.imshow('shapes', image)

cv.waitKey(0)
cv.destroyAllWindows()