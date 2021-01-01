#fotografin icinden bir kesit alip baska bir bolgeye kopyalamak

import cv2
import numpy as np

img = cv2.imread("lena.jpg")                                 #resimi okuyalim
print("shape of the photo :\n" , img.shape)                  #resmin boyutlarini gorelim
cv2.imshow("original", img)                                  #orjinal resmi bencerede gosterelim

b,g,r = cv2.split(img)                                   #orjinal resmin bilgilerini kopyalayalim
img1 = cv2.merge((b,g,r))                               #kopyalanan bilgilerle yeni bir klon olusturalim
cv2.imshow("klon",img1)                          #klon'u gosterelim

eye = img[240:300 , 290:350]                     #original resmin bir parcasini kopyalayalim

img1[253:313 , 80:140] = eye                #kopyalanmis parcayi, original resme...
cv2.imshow("shoped", img1)                       #... biraz buyutup yapistiralim

img1[203:263 , 60:120] = eye                            #kopyalanmis parcayi, original resme...
cv2.imshow("shoped", img1)                           #... biraz buyutup yapistiralim

cv2.imshow("goz", eye)                             #kopyaladigimiz parcayi gosterelim

key = cv2.waitKey() & 0xFF
if key == ord('q'):
    cv2.destroyAllWindows()