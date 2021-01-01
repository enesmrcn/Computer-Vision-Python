#deneme 24 - HSV (1/3)
#renkli toplarin arasindan mavi olanlari secmek
#inRange() kullanilacak

import cv2
import numpy as np

while True :
    img = cv2.imread('smarties.png')

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_b = np.array([91, 113, 113])
    u_b = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, l_b, u_b)

    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('original', img)
    cv2.imshow('blue_balls', result)

    key = cv2.waitKey(1) & 0xFF
    if key == 27 :
        break

cv2.destroyAllWindows()