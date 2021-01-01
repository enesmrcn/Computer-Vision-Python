import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg')

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    #cv.imshow('gaussian '+str(i+1), layer)


layer = gp[5]
lp = [layer]

for i in range(5, 0, -1):
    extended_gaussian = cv.pyrUp(gp[i])
    laplacian = cv.subtract(extended_gaussian, gp[i-1])
    lp.append(laplacian)
    cv.imshow('laplacian '+ str(i-1), laplacian)


cv.waitKey(0)
cv.destroyAllWindows()