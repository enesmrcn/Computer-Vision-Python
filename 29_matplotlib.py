#matplotlib kutuphanesini deneyelim

from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread('lena.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)   #fotoyu pencerede acmak
#plt.xticks([]), plt.yticks([])   #istersen kaldir/ekle. Fotonun etrafindaki koordinat cizgilerini siler
plt.show()          #


cv.waitKey(0)
cv.destroyAllWindows()

#_____________________________________________________________________


img = cv.imread('sudoku.png', 0)

__, normal = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 3)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 3)

img1 = cv.imread('smarties.png', 0)

__, TH = cv.threshold(img1,  127, 255, cv.THRESH_BINARY)
TH1 = cv.adaptiveThreshold(img1, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 11)

titles = ['img', 'basic_threshold', 'mean_threshlod', 'gaussian_th', 'normal_th', 'gaussian_th']
images = [img, normal, th1, th2, TH, TH1]

for i in range(6):
    plt.subplot(2,3, i+1) , plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]) , plt.yticks([])

cv.waitKey(0)
plt.show()
cv.destroyAllWindows()