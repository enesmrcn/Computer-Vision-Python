#tiklanan noktanin rengini ayri bir ekranda gosterir

import cv2
import numpy as np

def click_event(event, x, y, flags, param) :
    if event == cv2.EVENT_LBUTTONDOWN :
        red = img[y,x,2]
        green = img[y,x,1]
        blue = img[y,x,0]
        colorImage = np.zeros((100,100,3),np.uint8)
        colorImage[:] = [blue, green ,red]
        cv2.imshow("color", colorImage)

img = cv2.imread("lena.jpg",1)
cv2.imshow("lena" , img)
cv2.setMouseCallback("lena",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()