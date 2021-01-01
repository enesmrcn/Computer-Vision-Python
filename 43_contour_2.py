import cv2 as cv

img = cv.imread('opencv-logo.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

__, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

img1 = img.copy()
cv.imshow('pencere', img)
cv.waitKey(3000)
count = 1
while True:
    if count >= (len(contours) ):
        cv.imshow('pencere', img)
        cv.waitKey(3000)
        img1 = img.copy()
        count = 0

    cv.drawContours(img1, contours, count, (10, 100, 255), 4)
    cv.imshow('pencere', img1)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    cv.waitKey(2000)

    count += 1

cv.waitKey(0)
cv.destroyAllWindows()