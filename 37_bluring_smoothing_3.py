# bluring and smoothing (3/3)
#gaussian blur uygulandiktan sonra bilateral filter yapilmasi...

import cv2
import numpy as np
from matplotlib import pyplot as plt

count = 0

while True :

    if count == 0 :
        img = cv2.imread('messi.jpg')  #lena.jpg
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
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
    gaussianBlur = cv2.GaussianBlur(img, (5,5), 0)
    bilateralFilter = cv2.bilateralFilter(gaussianBlur, 9, 75, 75)

    titles = ['image', 'GaussianBlur', 'BilateralFilter']
    images = [img, gaussianBlur, bilateralFilter]

    for i in range(3):
        plt.subplot(1,3, i+1) , plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]) , plt.yticks([])

    plt.show()

    count += 1