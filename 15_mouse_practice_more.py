#foto uzerinde tikalanan yere kucuk bir daira (ici boyali) cizer
#son basilan daire ile henuz basilan daireyi bir line ile birlestirir

import cv2

font = cv2.FONT_HERSHEY_SIMPLEX      #yazi basarken kullanacagiz
line = cv2.LINE_AA                  #yazi basarken kullanacagiz
points = []

def take_photo():                   #bu minik fonksiyon yalnizca kamerandan fotograf cekmene yarar
    cap = cv2.VideoCapture(0)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
        if ((frame[10, 10, 1] != 0) or (frame[10, 20, 2] != 0) or (frame[100, 10, 0] != 0)):
            cv2.waitKey(5000)
            cv2.imwrite("screen_shot.png", frame)
            break
    cap.release()
    cv2.destroyAllWindows()

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(img, (x,y), 7, (0,0,255), -1, line)
        points.append((x,y))
        if len(points) >= 2 :
            cv2.line(img, (points[-1]), points[-2], (255,0,0), 1, line)
        cv2.imshow("screen", img)


take_photo()

img = cv2.imread("screen_shot.png", 1)
cv2.imshow("screen",img)

cv2.setMouseCallback("screen",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()