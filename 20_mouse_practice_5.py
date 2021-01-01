#foto uzerinde tikladigin her noktada minik ici boyali daire cikarir
#son tiklanan daire ile bir onceki arasinda cizgi olusturur
#olusturulan dairelerin yaninda koordinatlari gosterir
#bir tusa basica cixim renklerini degistirir
#bir tusa basinca resmi restler (cizimleri siler)
#bir tusa basinca projeyi kapatir
#bir tusa basinca projeyi kayit eder


import cv2
import numpy as np

def click_event(event, x, y, flags, param) :
    if event == cv2.EVENT_LBUTTONDBLCLK :
        cv2.circle(img, (x, y), 5, (255, 255, 255), -1, cv2.LINE_AA)
        points.append((x,y))
        print(colors[color_count], '\t', color_count)
        if len(points) > 1 :
            cv2.line(img, points[-2], points[-1], colors[color_count], 1, cv2.LINE_AA)

        cv2.imshow(name, img)

img = np.zeros((512, 512, 3), np.uint8)
count = 0
color_count = 0
colors = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (123, 10, 145), (200, 255, 255), (255, 0, 255)]
points = []

name = input('\nname the project of the name : \n')

while True :
    cv2.imshow(name, img)

    cv2.setMouseCallback(name, click_event)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r') :
        cv2.putText(img, 'reset', (200, 230), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 2)
        cv2.imshow(name, img)
        cv2.waitKey(2500)

        img = np.zeros((512, 512, 3), np.uint8)
        cv2.imshow(name, img)
        del points
        points = []
        key = 0
    elif key == ord('s') :
        string = "project_" + str(count) + '.jpg'
        cv2.imwrite(string, img)
        key = 0
    elif key == ord('c') :
        color_count += 1
        if color_count >= 5 :
            color_count = 0
        key = 0
    elif key == 27:
        break

cv2.destroyAllWindows()