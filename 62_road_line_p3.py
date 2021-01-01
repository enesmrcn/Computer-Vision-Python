#hintli dayi = line detection project - part3
#kodlar bana ait - orjinali icin Hintli Dayi'yi izle



import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def crop_roi(img, vertices):
    mask = np.zeros_like(img)
    cv.fillPoly(mask, vertices, 255)
    masked_image = cv.bitwise_and(mask, img)
    return masked_image


def drow_lines(canny_img, original_image):
    img_coppied = np.copy(original_image)
    img_lines = np.copy(original_image)    # lets show each lines
    lines = cv.HoughLinesP(canny_img, rho=10, theta=np.pi/160, threshold=160,
                           lines=np.array([]),
                           minLineLength=40,
                           maxLineGap=20)
    for line in lines :
        x1, y1, x2, y2 = line[0]
        cv.line(img_coppied, (x1, y1), (x2, y2), (255, 0, 0), 4, cv.LINE_AA)
        cv.circle(img_lines, (x1, y1), 10, (0, 255, 0), -1)
        cv.circle(img_lines, (x2, y2), 10, (0, 255, 0), -1)
        #print(line[0])      # optional

    return img_coppied, img_lines



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


gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
canny_image = cv.Canny(gray_image, 100, 200)
cropped_image = crop_roi(img=canny_image, vertices=np.array([roi_vertices], dtype=np.int32))

image_with_lines, show_the_lines = drow_lines(canny_img=cropped_image, original_image=image)



plt.subplot(2, 3, 1), plt.imshow(image)
plt.title('original image')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 2), plt.imshow(gray_image, 'gray')
plt.title('gray image')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 3), plt.imshow(canny_image, 'gray')
plt.title('canny image')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 4), plt.imshow(cropped_image, 'gray')
plt.title('cropped image')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5), plt.imshow(image_with_lines)
plt.title('lines')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6), plt.imshow(show_the_lines)
plt.title('circle')
plt.xticks([]), plt.yticks([])

plt.show()
