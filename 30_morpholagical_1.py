#morpholgical transformations (1/2)

import cv2
import numpy as np

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)

__, mask =cv2.threshold(img, 220, 250, cv2.THRESH_BINARY_INV)

kern = np.ones((2,2), np.uint8)

dilation = cv2.dilate(mask, kern, iterations=1)
erosion = cv2.erode(mask, kern, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kern, iterations=1)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kern, iterations=1)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kern, iterations=1)
th = cv2. morphologyEx(mask, cv2.MORPH_TOPHAT, kern, iterations=1)

cv2.imshow('mask', mask)
cv2.imshow('dilation', dilation)
cv2.imshow('erode', erosion)
cv2.imshow('opening', opening)
cv2.imshow('closing', closing)
cv2.imshow('GRADIENT', mg)
cv2.imshow('TOPHAT', th)


cv2.waitKey(0)
cv2.destroyAllWindows()