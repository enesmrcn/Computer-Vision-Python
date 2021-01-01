#ekranin genislik uzunluk ayarlamasi
#gosterilecek olan ekranin buyuklugunu kullanici belirlesin
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)  veya cap.set(3, 1200)
#cap.get(3) veya cap.get(cv2.CAP_PROP_FRAME_WIDTH)

import cv2


choise = input("\nwhich video do yu wanna watch?\nbeautiful\nfunny\n")
choise = choise.lower()
width = 0
height = 0
fps = 0
count = 0

if (choise == "beautiful") :
    cap = cv2.VideoCapture("video_2.mp4")
elif (choise == "funny") :
    cap = cv2.VideoCapture("video_1.mp4")
else :
    print("\nInvalid choise! Default video opening!\n")
    cap = cv2.VideoCapture("naber.mov")

width = int(input("\nchoose the width\n"))
height = int(input("\nchoose the height"))
fps = int(input("\nchoise the FPS\n"))
mode = input("\n\nwhich mode do you want:\nstandard\ngray\ncolored\nblue\n")

cap.set(3,width)
cap.set(4,height)
cap.set(cv2.CAP_PROP_FPS, fps)



while (cap.isOpened()) :
    ret, frame = cap.read()


    if (cv2.waitKey(1) & 0xFF == ord('q')) :
        break


    if count == 0:
        filtered = cv2.cvtColor(frame, cv2.COLORMAP_JET)  # standard
    elif count == 1:
        filtered = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # gray
    elif count == 2:
        filtered = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)  # gray
    elif count == 3:
        filtered = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # gray

    if (cv2.waitKey(1) & 0xFF == ord('c')) :
        count+= 1
        if count == 4:
            count = 0


    cv2.imshow("ekran", filtered)

cap.release()
cv2.destroyAllWindows()