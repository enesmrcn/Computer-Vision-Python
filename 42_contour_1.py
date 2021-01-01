import cv2 as cv

img = cv.imread('opencv-logo.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

__, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
contour, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
cv.drawContours(img, contour, -1, (0, 124, 255), 4)

cv.imshow('pencere', img)

cv.waitKey(0)
cv.destroyAllWindows()