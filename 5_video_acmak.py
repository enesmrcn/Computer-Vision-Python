#opens a video ("comeon.mov")
#it can record in different modes and filters
#you can quit the window by clicking 'q'

import cv2
import numpy as np

video = cv2.VideoCapture('video_1.mp4')
mod = 1  # video modu degiskeni

if (video.isOpened()):  # video acilabilirse
    print("\nvideo is opening...\n")
else:
    print("\nthe source file could not found\n")

while (video.isOpened()):
    __, frame = video.read()

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        key = 0
        mod += 1
        if mod == 5:
            mod = 0
    elif key == 27:
        break

    if mod == 0:
        img = frame
    elif mod == 1:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    elif mod == 2:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    elif mod == 3:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif mod == 4:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)
    else:
        mod = 0

    cv2.imshow('ekran', img)

video.release()
cv2.destroyAllWindows()