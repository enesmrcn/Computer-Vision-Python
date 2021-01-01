# deneme 21 --version (3/3)
#trackbar uzerinde calisacagiz
#tracbar uzerindeki sayiyi degistirdikce , bunun degeri fotografa basilacak
#ayrica bir buton fotoya filtre uygulayabilecek
#NOT: fotografa basilan yazilarin renginin filtre ile degismesini istemiyorsan , yazi kodlarini filtreden sonra koy

import cv2 as cv
import numpy as np
import datetime as dt

def func(x) :
    print(x)

#img = np.zeros((512,512,3),np.uint8)   #eger bu kod'u asagidakinin yerine burada calistirsaydin....
                                        #...neyse ne olurdu kendin gor
cv.namedWindow('window')

cv.createTrackbar('parameter','window',10,1024,func)
mode = 'colored/gray/standard'
cv.createTrackbar(mode, 'window', 0, 2, func)

while True :
    img = cv.imread('lena.jpg')  #img = np.zeros((512, 512, 3), np.uint8)  ile degistirdim
    img = cv.resize(img, (720,720))

    param = cv.getTrackbarPos('parameter', 'window')
    cv.putText(img, str(param), (300, 300), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 4)
    #cv.putText(img, str(dt.datetime.now()), (50,50), cv.FONT_HERSHEY_SIMPLEX, 1, (255,120,2), 1) #tarih basar. istersen sil

    filter = cv.getTrackbarPos(mode, 'window')
    if filter == 0:
        img = cv.cvtColor(img,cv.COLOR_RGB2BGR)
    elif filter == 1 :
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    elif filter == 2 :
        img = cv.cvtColor(img, cv.COLOR_RGB2HSV)

    cv.imshow('window',img)

    key = cv.waitKey(1) & 0xFF
    if key == 27 :
        break

cv.destroyAllWindows()