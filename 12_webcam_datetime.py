#ekranda cozunurlugun yani sira FPS ve tarih-saat basan progtam yaz

import cv2
import datetime as dt

cap = cv2.VideoCapture(0)

if (cap.isOpened()):
    print("\nvideo is playing...")
else:
    print("\nthe cam could not opened\terror : #1")

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        date = dt.datetime.now()
        print("\t", date)

        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        frame = cv2.putText(frame, str(date), (60, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 0, 255), 1, cv2.LINE_AA)
        frame = cv2.rectangle(frame, (40, 25), (580, 80), (0, 255, 0), 2, cv2.LINE_AA)

        text1 = str(int(height)) + 'x' + str(int(width))
        frame = cv2.putText(frame, text1, (60, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 1, cv2.LINE_AA)
        frame = cv2.rectangle(frame, (40, 100), (220, 140), (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow("signal", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
    else:
        print("\bno signal from the camera\terror : #2")

cap.release()
cv2.destroyAllWindows()