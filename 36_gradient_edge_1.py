#gradient & edge detection (1/2)

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

org = cv.imread('messi5.jpg')
org = cv.cvtColor(org, cv.COLOR_BGR2RGB)
img = cv.imread('messi5.jpg', cv.IMREAD_GRAYSCALE)

lap = cv.Laplacian(img, cv.CV_64F, ksize=1)
lap = np.uint8(np.absolute(lap))

sobelX = cv.Sobel(img, cv.CV_64F, 0, 1)
sobelY = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

combination = cv.bitwise_or(sobelY, sobelX)

images = [org, img, lap, sobelX, sobelY, combination]
titles = ['original', 'GRAYSCALE', 'LAPLACIAN', 'SOBEL_X', 'SOBEL_Y', '( sobel_X + sobel_Y )']

for i in range(6) :
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])

plt.show()