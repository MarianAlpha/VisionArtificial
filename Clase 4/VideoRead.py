import cv2

cap = cv2.VideoCapture('Video.avi')

while True:

    ret, frame = cap.read()

    print(ret)

    cv2.imshow('Video', frame)

    t = cv2.waitKey(1)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()