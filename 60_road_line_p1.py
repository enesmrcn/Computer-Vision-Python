#hintli dayi = line detection project - part1
#kodlar bana ait - orjinali icin Hintli Dayi'ui izle
# roi (region of interest) icin fotografi kirpmak

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def crop_roi(img, channel, vertices):
    mask = np.zeros_like(img)
    cv.fillPoly(mask, vertices, (255, 255, 255))
    masked_image = cv.bitwise_and(mask, img)
    return masked_image

image = cv.imread('road4test2.png')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)


height = image.shape[0]
width = image.shape[1]
channel_count = image.shape[2]

roi_vertices = [
    (260, height),
    (1280, 980),
    (1760, 980),
    (width, height)
]


cropped_image = crop_roi(img=image, channel=channel_count, vertices=np.array([roi_vertices], dtype=np.int32))

plt.subplot(1, 2, 1), plt.imshow(image)
plt.title('original image')
plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(cropped_image)
plt.title('cropped image')
plt.show()