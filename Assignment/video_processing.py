import cv2

cap = cv2.VideoCapture('video/v3.mp4')
i = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    a = i / 17
    for b in range(50):
        if (a == b):
            cv2.imwrite(str(a) + '.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()