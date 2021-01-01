#CANNY DETECTION

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.png', cv2.IMREAD_GRAYSCALE)


canny1 = cv2.Canny(img, 100, 200)
canny2 = cv2.Canny(img, 100, 200)
canny3 = cv2.Canny(img, 100, 200)

img1 = cv2.imread('messi.jpg', 0)

canny11 = cv2.Canny(img1, 100, 200)
canny22 = cv2.Canny(img1, 100, 200)
canny33 = cv2.Canny(img1, 100, 200)

images = [img, canny1, canny2, canny3, img1, canny11, canny22, canny33]
title = ['original', 'canny (1)', 'canny (2)', 'canny (3)', 'origianal', 'canny 1', 'canny 2', 'canny 3']

for i in range(8) :
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(title[i])

plt.show()