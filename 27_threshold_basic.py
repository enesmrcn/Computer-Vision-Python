#basit treshold islemleri

import cv2
import numpy as np

#%%

img = cv2.imread('gradient.png')

__, th1 = cv2.threshold(img, 124, 255, cv2.THRESH_BINARY)
__, th2 = cv2.threshold(img, 124, 255, cv2.THRESH_BINARY_INV)
__, th3 = cv2.threshold(img, 124, 255, cv2.THRESH_TRUNC)
__, th4 = cv2.threshold(img, 124, 255, cv2.THRESH_TOZERO)
__, th5 = cv2.threshold(img, 124, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.imshow('th4', th4)
cv2.imshow('th5', th5)

cv2.waitKey(0)
cv2.destroyAllWindows()

#%%

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('gradient.png', cv.IMREAD_GRAYSCALE)

__, th1 = cv.threshold(img, 125, 255, cv.THRESH_BINARY)
__, th2 = cv.threshold(img, 125, 255, cv.THRESH_BINARY_INV)
__, th3 = cv.threshold(img, 125, 255, cv.THRESH_TOZERO)
__, th5 = cv.threshold(img, 125, 255, cv.THRESH_TOZERO_INV)
__, th4 = cv.threshold(img, 125, 255, cv.THRESH_TRUNC)

images = [img, th1, th2, th3, th5, th4]
titles = ['original', 'THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_TOZERO', 'THRESH_TOZERO_INV', 'THRESH_TRUNC']

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()