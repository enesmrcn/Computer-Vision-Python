import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

g_lyr1 = cv.pyrDown(img)
g_lyr2 = cv.pyrDown(g_lyr1)
g_lyr3 = cv.pyrDown(g_lyr2)

lp_lyr1 = cv.pyrUp(g_lyr3)
lp_lyr2 = cv.pyrUp(g_lyr2)
lp_lyr3 = cv.pyrUp(g_lyr1)

laplacian1 = cv.subtract(g_lyr2, lp_lyr1)
laplacian2 = cv.subtract(g_lyr1, lp_lyr2)
laplacian3 = cv.subtract(lp_lyr3, img)

images = [img, g_lyr1, g_lyr2, g_lyr3, lp_lyr1, lp_lyr2, lp_lyr3, laplacian1, laplacian2, laplacian3]
titles = ['original', 'gaussian_1', 'gaussian_2', 'gausissian_3', 'lp_1', 'lp_2', 'lp_3', 'laplacian1', 'laplacian2',
          'laplacian3']

for i in range(10):
    plt.subplot(3, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])

plt.show()