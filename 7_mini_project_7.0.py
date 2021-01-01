#OPENCV UYGULAMA 7 --version 1
#getting width and height properties from the live-cam
#take the screen shot by clicking 's'
#exit the windows by clicking 'q'
#@enes mercan

import cv2
import numpy as np

choise = 0
count = 0

cap = cv2.VideoCapture(0);
if cap.isOpened() :
    print("\nVideo opening....\n")
    choise = int(input("\nwhich filter do you want to use?\n1 : Gray\n2 : Blue\n3 : Other\n"))
else :
    print("\nVideo path-way is wrong!\n")

while (cap.isOpened()):
    ret,frame = cap.read()

    if choise == 1 :
     mode = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #GRy
    elif choise == 2 :
     mode = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) #blue
    elif choise == 3 :
     mode = cv2.cvtColor(frame, cv2.COLOR_HSV2RGB) #Gotkusagi
    else :
     mode = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("vide0 : %4d x %4d\t"%(width,height))

    cv2.imshow("ekran" , mode)

    if (cv2.waitKey(1) & 0xFF == ord('q')) :
        break
    if (cv2.waitKey(1) & 0xFF == ord('s')) :
        string = "screen_shot_" + str(count) + ".png"
        cv2.imwrite(string , mode)
        count += 1
cap.release()
cv2.destroyAllWindows()