#bir fotodaki renkleri cek (red,green,blue) [split metodu ile]
#bu renklere ait array'leri  birlestirerek baska bir foto yarat [merge metodu]
#sonuc olarak bu uygulamada foto klonlamayi gorecegiz

import cv2

img1 = cv2.imread("lena.jpg")
b,g,r = cv2.split(img1)      #renkleri ayri ayri b , g , r dizilerine yapistirdik

img2 = cv2.merge((b,g,r))

cv2.imshow("orjinal foto", img1)
cv2.imshow("klon foto", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()