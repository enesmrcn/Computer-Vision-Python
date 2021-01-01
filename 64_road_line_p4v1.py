# hintli dayi = line detection project - part4
# kodlar bana ait - orjinali icin Hintli Dayi'yi izle



import cv2 as cv
import numpy as np

def crop_roi(img, vertices):
    mask = np.zeros_like(img)
    cv.fillPoly(mask, vertices, 255)
    masked_image = cv.bitwise_and(mask, img)
    return masked_image


def drow_lines(canny_img, original_image):
    img_coppied = np.copy(original_image)
    img_lines = np.copy(original_image)  # lets show each lines
    lines = cv.HoughLinesP(canny_img, rho=10, theta=np.pi / 160, threshold=160,
                           lines=np.array([]),
                           minLineLength=40,
                           maxLineGap=20)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img_coppied, (x1, y1), (x2, y2), (0, 0, 255), 5, cv.LINE_AA)
        cv.circle(img_lines, (x1, y1), 10, (0, 0, 255), -1)
        cv.circle(img_lines, (x2, y2), 10, (0, 0, 255), -1)
        # print(line[0])      # optional

    return img_coppied, img_lines



video2 = 'test2.mov'

cap = cv.VideoCapture(video2)

ret, frame = cap.read()

while cap.isOpened() :

    ret, frame = cap.read()


    image = np.copy(frame)

    height = image.shape[0]
    width = image.shape[1]
    channel_count = image.shape[2]

    roi_vertices = [
        (95, height),
        (1091, 840),
        (1416, 840),
        (1865, 1358),
    ]


    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    canny_image = cv.Canny(gray_image, 100, 200)
    cropped_image = crop_roi(img=canny_image, vertices=np.array([roi_vertices], dtype=np.int32))

    image_with_lines, show_the_lines = drow_lines(canny_img=cropped_image, original_image=image)

    cv.imshow('video', image_with_lines)

    key = cv.waitKey(10) & 0xFF
    if key == ord('q') :
        break


cap.release()
cv.destroyAllWindows()