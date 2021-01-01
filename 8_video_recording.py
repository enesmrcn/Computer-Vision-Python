#recording a video source

import cv2
import numpy as np

cap = cv2.VideoCapture(0)


count = 0
string_count = 0

while (cap.isOpened()) :
    ret, frame = cap.read()

    if ret :
        cv2.imshow('pencere_ismi', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s') :
            if count == 0 :
                string_count += 1
                prop = str(int(cap.get(cv2.CAP_PROP_FPS))) + '_' + str(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))) + 'x' + str(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
                string = "recorded_video_" + str(string_count) + "_fps_" + prop + '.avi'
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                out = cv2.VideoWriter(string, fourcc, 20, (480, 640))
                out.write(frame)
                count = 1
            elif count :
                out.release()
                count = 0


            key = 0

        elif key == ord('q') :
            break


    else :
        break

out.release()
cap.release()
cv2.destroyAllWindows()