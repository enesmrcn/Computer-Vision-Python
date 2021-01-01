# cekilen canli videonun genislik-yukseklik bilgisini ekrana basan program

import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
line = cv2.LINE_AA

cap = cv2.VideoCapture(0)

if (cap.isOpened()) :
    print("\nCam is opening....\n")
else :
    print("\nCam could't find! error_code : 1")  #error_code : 1

while (cap.isOpened()) :
    ret, frame = cap.read()

    width = cap.get(3)
    height = cap.get(4)


    string_width = "width : " + str(int(width))
    string_height = "height : " + str(int(height))
    cv2.putText(frame, string_width, (40,40), font, 0.9, (255,255,0), 1, line)
    cv2.putText(frame, string_height, (40,70), font, 0.9, (255,255,0), 1, line)

    cv2.imshow("ekran", frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')) :
        break

cap.release()
cv2.destroyAllWindows()