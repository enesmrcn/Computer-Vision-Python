import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('pyramid.png')
original = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv.cornerHarris(gray, 2, 3, 0.04)
corners = cv.dilate(corners, None, iterations=3)        #dilation to mark corners

img[corners > (0.009 * corners.max())] = [0, 0, 255]  #thresholding


img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.subplot(1, 2, 1), plt.imshow(original)
plt.title("original")
plt.subplot(1, 2, 2), plt.imshow(img)
plt.title("corners")

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()