# deneme 21 --version (1/3)
#trackbar uzerinde calisacagiz

import cv2 as cv
import numpy as np

def paint(x):
    print(x)

img = np.zeros((512,512,3),np.uint8)        #siyah resim olusturalim

cv.namedWindow("window")             #yeni bir pencere olusturalim

cv.createTrackbar('Blue','window', 0, 255, paint)
cv.createTrackbar('Green', 'window', 0, 255, paint)
cv.createTrackbar('Red', 'window', 0, 255, paint)

while True :
    cv.imshow('window', img)
    key = cv.waitKey(1) & 0xFF
    if key == 27 :
        break
cv.destroyAllWindows()
