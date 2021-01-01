#display image with different filters

import cv2
import numpy as np

img1 = cv2.imread('lena.jpg' , 0)
print(img1)
cv2.imshow('renkli', img1)
cv2.waitKey(5000)
cv2.destroyAllWindows()

img2 = cv2.imread('lena.jpg' , 1)
print(img2)
cv2.imshow('gray_scale', img2)
cv2.waitKey(5000)
cv2.destroyAllWindows()

img3 = cv2.imread('lena.jpg', -1)
print(img3)
cv2.imshow('alpha_chajnnle', img3)
cv2.waitKey(5000)
cv2.destroyAllWindows()