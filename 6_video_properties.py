#getting width and height properties from the video

import cv2
import numpy as np

cap = cv2.VideoCapture("naber.mov")
print(cap.isOpened())

while (cap.isOpened()) :
    ret, frame = cap.read()
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    cv2.imshow("ekran",frame)
    print("width :\t%d\t\theight :\t%d"%(width,height))
    if (cv2.waitKey(1) & 0xFF == ord('q')) :
        break
cap.release()
cv2.destroyAllWindows()