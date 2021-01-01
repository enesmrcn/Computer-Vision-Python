#fotograf uzerinde calis
#left click yapinca kordinatlari verir
#right click yapinca rgb verir
#programda kullanilacak forografi pc kamerandan cekip kaydetme ozelligi vardir (komple otomatik)

import cv2

font = cv2.FONT_HERSHEY_SIMPLEX      #yazi basarken kullanacagiz
line = cv2.LINE_AA                  #yazi basarken kullanacagiz
secim = 0

secim = int(input("\nkamerandan fotograf cekecegim veya hazir foto kullanacagim."
                  "Sec birini\n1) Kamera\n2)Hazir foto\n"))

def take_photo():                   #bu minik fonksiyon yalnizca kamerandan fotograf cekmene yarar
    cap = cv2.VideoCapture(0)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
        if ((frame[10, 10, 1] != 0) or (frame[10, 20, 2] != 0) or (frame[100, 10, 0] != 0)):
            cv2.imwrite("screen_shot.png", frame)
            break
    cap.release()
    cv2.destroyAllWindows()

def click_event(event, x, y, flags, param) :
    if event == cv2.EVENT_LBUTTONDOWN :
        coordinates = "(" + str(x) + "," + str(y) + ")"
        cv2.putText(img, coordinates, (x,y), font, 0.7, (255,255,0), 2, line)
        cv2.imshow("ekran", img)
    if event == cv2.EVENT_LBUTTONUP:
        red = img[y,x,2]
        green = img[y,x,1]
        blue =  img[y,x,0]
        rgb_param = "(" + str(int(red)) + "," + str(int(green)) + "," + str(int(blue)) + ")"
        cv2.putText(img, rgb_param, ((x+10),(y+20)), font, 0.7, (0,255,255), 2, line)
        cv2.imshow("ekran",img)

if secim == 1 :
    take_photo()
    img = cv2.imread("screen_shot.png", 1)
elif secim == 2 :
    print("\nO zaman ayni dosya dizininde lena.jpg adli  bir resim bulundurmalisin\n")
    img = cv2.imread("lena.jpg", 1)


cv2.imshow("ekran", img)
cv2.setMouseCallback("ekran",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
