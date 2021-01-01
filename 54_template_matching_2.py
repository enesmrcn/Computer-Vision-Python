import cv2 as cv
import numpy as np

img_rgb = cv.imread('mario.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('mario_template.png', cv.IMREAD_GRAYSCALE)


res = cv.matchTemplate(img_gray, template, cv.TM_CCORR_NORMED)

threshold = 0.9

loc = np.where(res >= threshold)

print(res)              # optional
print("\n\n",loc)           # optional
minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(res)        # optional
print('\nmax value :\t', maxVal,"\nmin value :\t", minVal)       # optional

width, height = template.shape[::-1]

for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + width, pt[1] + height), (0,0,255), 2)

cv.imshow('matcehd', img_rgb)
cv.waitKey(0)
cv.destroyAllWindows()