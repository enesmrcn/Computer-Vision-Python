#left click yapinca kordinatlari verir
#right click yapinca rgb verir
#basitlesitirlmis ornektir. Sonraki daha complex

import cv2
import numpy as np

def click_event(event, x, y, flags, params) :
    if event == cv2.EVENT_LBUTTONDBLCLK :
        coords = '(' + str(x) + ',' + str(y) + ')'
        cv2.putText(img, coords, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0))
        cv2.imshow('ekran', img)
    elif event == cv2.EVENT_LBUTTONDOWN :
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        text = '(' + str(b) + ',' + str(g) + ',' +str(r) + ')'
        cv2.putText(img, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
        cv2.imshow('ekran', img)

img = cv2.imread('lena.jpg')

cv2.imshow('ekran', img)
cv2.setMouseCallback('ekran', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()