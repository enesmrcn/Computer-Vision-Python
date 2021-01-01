#save the image

import cv2
import numpy as np

img = cv2.imread('lena.jpg', 0)
cv2.imshow('new', img)
k = cv2.waitKey(0) & 0xFF

if k == 27 :
    cv2.destroyAllWindows()
elif k == ord('s') :
    cv2.imwrite('new_image.png', img)
    cv2.destroyAllWindows()