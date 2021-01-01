#deneme 24 - HSV (3/3)

import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)

cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while True :
    __, img = cap.read()
    img = cv2.resize(img, (720,512))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')
    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('original', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('the_musk', mask)
    cv2.imshow('filtered', result)

    key = cv2.waitKey(1) & 0xFF
    if key == 27 :
        break

cap.release()
cv2.destroyAllWindows()