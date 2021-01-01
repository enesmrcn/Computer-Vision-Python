#open live-stream with build-in cam
#you can quit the window by clicking 'q'

import cv2
import numpy as np

deneme = cv2.VideoCapture(0)

while (True) :
    ret,video = deneme.read()
    cv2.imshow("ekran" , video)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

deneme.release()
cv2.destroyAllWindows()