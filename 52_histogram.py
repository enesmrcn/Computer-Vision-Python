import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt



def func(count) :

    if count == 1 :
        img_gray = cv.imread('lena.jpg', 0)
        plt.hist(img_gray.ravel(), 256, [0, 256])

        cv.imshow('lena_gray', img_gray)
        plt.show()
        cv.waitKey(0)
        cv.destroyAllWindows()


    elif count == 2 :
        img_colored = cv.imread('lena.jpg')

        plt.hist(img_colored.ravel(), 256, [0, 256])
        cv.imshow('lena_colored', img_colored)
        plt.show()

        cv.waitKey(0)
        cv.destroyAllWindows()

    elif count == 3 :
        img_bgr = cv.imread('lena.jpg')

        (b, g, r) = cv.split(img_bgr)
        cv.imshow('b', b)
        cv.imshow('g', g)
        cv.imshow('r', r)

        plt.hist(b.ravel(), 256, [0, 256])
        plt.hist(g.ravel(), 256, [0, 256])
        plt.hist(r.ravel(), 256, [0, 256])
        plt.show()

        cv.waitKey(0)
        cv.destroyAllWindows()

count = 0
while count <= 3 :
    cv.destroyAllWindows()
    count +=1
    func(count)
    cv.waitKey(0)