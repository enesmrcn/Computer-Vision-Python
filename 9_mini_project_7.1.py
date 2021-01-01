#OPENCV UYGULAMA 7 --version 2
#getting width and height properties from the live-cam
#take the screen shot by clicking 's'
#exit the windows by clicking 'q'

import cv2
import numpy as np

def choises() :
    choise = int(input("\n1 : Gray\n2 : Colored \n3: any"))
    return choise

cap = cv2.VideoCapture(0)

if cap.isOpened():
    print("\nCam is opening....\n")
    count = 0
    choise = choises()
    cv2.waitKey(50000)
else :
    print("\nCam could not find !\n")

while (cap.isOpened()) :
    ret, frame = cap.read()

    if (choise == 1) :
        mode = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        string = "gray mode"
    elif (choise == 2) :
        mode = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        string = "colored mode"
    elif (choise == 3) :
        mode = cv2.cvtColor(frame, cv2.COLORMAP_JET)
        string = "something mode"
    else :
        mode = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        string = "default mode"

    cv2.imshow(string ,mode)

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)

    if (cv2.waitKey(1) & 0xFF == ord('s')) :
        string1 = "screen_shot_" + str(count) +"_"+ str(width) + "x" + str(height) + "_fps" + str(fps) +" .jpeg"
        cv2.imwrite(string1, mode)
        count += 1
    if (cv2.waitKey(1) & 0xFF == ord('q')) :
        break

cap.release()
cv2.destroyAllWindows()