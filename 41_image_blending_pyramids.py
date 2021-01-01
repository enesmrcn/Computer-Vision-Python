import cv2 as cv
import numpy as np

apple = cv.imread('apple.jpg')
orange = cv.imread('orange.jpg')

print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))
cv.imshow('basic_technique', apple_orange)

###gaussian pyramid for apple

apple_layer = apple.copy()
gp_apple = [apple_layer]

for i in range(6):
    apple_layer = cv.pyrDown(apple_layer)
    gp_apple.append(apple_layer)
    # cv.imshow('apple_gaussian_'+str(i), apple_layer)

###gaussian pyramid for orange

orange_layer = orange.copy()
gp_orange = [orange_layer]

for i in range(6):
    orange_layer = cv.pyrDown(orange_layer)
    gp_orange.append(orange_layer)
    # cv.imshow('orange_gaussian_'+str(i), orange_layer)

###laplacian pyramid for apple

layer = gp_apple[5]
lp_apple = [layer]

for i in range(5, 0, -1):
    layer = cv.pyrUp(layer)
    laplacian = cv.subtract(layer, gp_apple[i - 1])
    lp_apple.append(laplacian)
    # cv.imshow('apple_laplacian_'+str(i), laplacian)

###laplacian pyramid for orange

layer = gp_orange[5]
lp_orange = [layer]

for i in range(5, 0, -1):
    layer = cv.pyrUp(layer)
    laplacian = cv.subtract(layer, gp_orange[i - 1])
    lp_orange.append(laplacian)
    # cv.imshow('orange_laplacian_'+str(i), laplacian)

###Now add right and left helves of images in each level

apple_orange_pyramid = []
n = 0

for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, __ = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols / 2)], orange_lap[:, int(cols / 2):]))
    apple_orange_pyramid.append(laplacian)

### now reconstruct them

apple_orange_reconstruct = apple_orange_pyramid[0]

for i in range(1, 6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv.imshow('sonuc', apple_orange_reconstruct)

cv.waitKey(0)
cv.destroyAllWindows()