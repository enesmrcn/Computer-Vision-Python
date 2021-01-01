#open live-stream with build-in cam
#you can take the screen shot by clicking 's'
#you can quit the window by clicking 'q'
import cv2
import numpy as np

count = 2
deneme = cv2.VideoCapture(0)

while (True) :
    ret,video = deneme.read()

    gray = cv2.cvtColor(video, cv2.COLORMAP_JET)  #changes the video color
    cv2.imshow('ekran', gray)

    #cv2.imshow("ekran" , video)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break
    if cv2.waitKey(1) & 0xFF == ord('s') :
        string = "screen_shot_" + str(count) + ".png"
        cv2.imwrite(string, gray)
        count+=1
deneme.release()
cv2.destroyAllWindows()