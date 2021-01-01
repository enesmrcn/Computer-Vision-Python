#iki farkli fotoyu birlestirmek
#add() ve addWeighted() kullanilacak

import cv2
import numpy as np

src1 = cv2.imread("lena.jpg")
src2 = cv2.imread("wifi.png")

print("\nsize of first image :\n",src1.shape)
print("size of second image :\n", src2.shape)

#new_img = cv2.add(src1, src2)        #Burasi onemli! Boyutlari ayni olmayan resimleri birlestiremessin

src1 = cv2.resize(src1, (512,512))
src2 = cv2.resize(src2, (512,512))

new_img = cv2.add(src1, src2)

#cv2.imshow("resim 1",src1)
#cv2.imshow("resim 2", src2)
cv2.imshow("new",new_img)

print("\nsize of first image :\n",src1.shape)
print("size of second image :\n", src2.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()