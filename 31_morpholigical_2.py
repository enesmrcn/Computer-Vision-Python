#morpholgical transformations (2/2)
#ayni islemler matplotlib kutuphanesi ile gosterilmistir

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)

__, mask =cv2.threshold(img, 220, 250, cv2.THRESH_BINARY_INV)

kern = np.ones((2,2), np.uint8)

dilation = cv2.dilate(mask, kern, iterations=1)
erosion = cv2.erode(mask, kern, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kern, iterations=1)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kern, iterations=1)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kern, iterations=1)
th = cv2. morphologyEx(mask, cv2.MORPH_TOPHAT, kern, iterations=1)

#titles = ['image','mask', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'tophat']
#images = ['img','mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'tophat']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2,4, i+1) , plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])


plt.show()