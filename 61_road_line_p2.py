#hintli dayi = line detection project - part2
#kodlar bana ait - orjinali icin Hintli Dayi'ui izle
#not: fotoyu once kesip sonra Canny yaptigin icin kenarlari da algilar

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def crop_roi(img, channel, vertices):
    mask = np.zeros_like(img)
    cv.fillPoly(mask, vertices, (255, 255, 255))
    masked_image = cv.bitwise_and(mask, img)
    return masked_image


def drow_lines(img):
    img_coppied = np.copy(img)
    img_lines = np.copy(img)    # lets show each lines
    gray_image = cv.cvtColor(img_coppied, cv.COLOR_RGB2GRAY)
    canny_image = cv.Canny(gray_image, 100, 200)
    lines = cv.HoughLinesP(canny_image, rho=10, theta=np.pi/160, threshold=160,
                           lines=np.array([]),
                           minLineLength=40,
                           maxLineGap=20)
    for line in lines :
        x1, y1, x2, y2 = line[0]
        cv.line(img_coppied, (x1, y1), (x2, y2), (255, 0, 0), 4, cv.LINE_AA)
        cv.circle(img_lines, (x1, y1), 10, (0, 255, 0), -1)
        cv.circle(img_lines, (x2, y2), 10, (0, 255, 0), -1)

    return (img_coppied, img_lines)



image = cv.imread('road4test2.png')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)


height = image.shape[0]
width = image.shape[1]
channel_count = image.shape[2]

roi_vertices = [
    (260, height),
    (1280, 980),
    (1720, 980),
    (2300, height)
]


cropped_image = crop_roi(img=image, channel=channel_count, vertices=np.array([roi_vertices], dtype=np.int32))

image_with_lines, show_the_lines = drow_lines(img=cropped_image)



plt.subplot(2, 2, 1), plt.imshow(image)
plt.title('original image')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2), plt.imshow(cropped_image)
plt.title('cropped image')

plt.subplot(2, 2, 3), plt.imshow(image_with_lines)
plt.title('lines')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4), plt.imshow(show_the_lines)
plt.title('circle')
plt.xticks([]), plt.yticks([])

plt.show()
