# bluring and smoothing (2/3)
#bol ornekli modu

import cv2
import numpy as np
from matplotlib import pyplot as plt

count = 0

while True :

    if count == 0 :
        img = cv2.imread('messi.jpg')  #lena.jpg
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (760, 480))
    elif count == 1 :
        img = cv2.imread('smarties.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif count == 2 :
        img = cv2.imread('wifi.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif count == 3 :
        img = cv2.imread('bird_40.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif count == 4 :
        img = cv2.imread('road2.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif count == 5 :
        img = cv2.imread('sudoku.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    else :
        break


    kernel = np.ones((5,5,), np.float32)/25
    dst = cv2.filter2D(img, -1, kernel)         #2d convolution
    blur = cv2.blur(img, (5,5))     #bluring
    gaussianBlur = cv2.GaussianBlur(img, (5,5), 0)
    median = cv2.medianBlur(img, 5)
    bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

    titles = ['image', '2D CONVOLUTION', 'BLURING', 'GaussianBlur', 'MEDIAN', 'bilateralFilter']
    images = [img, dst, blur, gaussianBlur, median, bilateralFilter]

    for i in range(6):
        plt.subplot(2,3, i+1) , plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]) , plt.yticks([])

    plt.show()

    count += 1