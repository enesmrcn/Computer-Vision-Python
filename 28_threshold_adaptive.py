#adaptive threshold islemleri
#3 farkli metod kullanarak verimliliklerini kiyaslayacagiz

import cv2
import numpy as np

img = cv2.imread('sudoku.png', 0)

__, normal = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 3)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 3)

cv2.imshow('normal_threshold', normal)
cv2.imshow('MEAN', th1)
cv2.imshow('GAUSSIAN', th2)

cv2.waitKey(0)
cv2.destroyAllWindows()

#_____________________________________________________________________

img1 = cv2.imread('smarties.png', 0)

__, TH = cv2.threshold(img1,  127, 255, cv2.THRESH_BINARY)
TH1 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 11)

cv2.imshow('normal', TH)
cv2.imshow('GAUSSIAN', TH1)

cv2.waitKey(0)
cv2.destroyAllWindows()