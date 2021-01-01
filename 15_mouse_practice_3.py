import cv2
import numpy as np


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x, y), 3, (255, 255, 0), 1, cv2.LINE_AA)
        points.append((x, y))
        if len(points) > 1:
            cv2.line(img, (x, y), points[-2], (255, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow('ekran', img)
    elif event == cv2.EVENT_LBUTTONDOWN:
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        color = np.zeros((480, 480, 3), np.uint8)
        color[:] = [b, g, r]
        cv2.imshow('new', color)


img = cv2.imread('lena.jpg')

cv2.imshow('ekran', img)
cv2.namedWindow('new')

points = []

cv2.setMouseCallback('ekran', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()