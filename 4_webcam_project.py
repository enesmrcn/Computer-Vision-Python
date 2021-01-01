#open live-stream with build-in cam
#it can record in different modes and filters
#you can quit the window by clicking 'q'

import cv2
import numpy as np

count = 0
cap = cv2.VideoCapture(0)

select = input("\nselect the mod :\nnormal\ngray\nblue\nlab\nhsv\n")

while (cap.isOpened() == True) :
    ret, frame = cap.read()


    if select == 'normal' :
        img = frame
    elif select == 'gray' :
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif select == 'blue' :
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    elif select == 'lab' :
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    elif select == 'hsv' :
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    else :
        print("\n!!!invalid input\n")
        break
    cv2.imshow('screen', img)


    key = cv2.waitKey(1) & 0xFF

    if key == 27 :
        break

    elif key == ord('s') :
        key = 0
        count += 1
        string = 'screen_shot_' + str(count) + '.png'
        cv2.imwrite(string, img)

    elif key == ord('c') :
        c = 0
        if select == 'hsv' :
            select = 'normal'
        elif select == 'lab' :
            select = 'hsv'
        elif select == 'blue' :
            select = 'lab'
        elif select == 'gray' :
            select = 'blue'
        elif select == 'normal' :
            select = 'gray'
        else :
            print("\n error code : #12")
            break

cap.release()
cv2.destroyAllWindows()