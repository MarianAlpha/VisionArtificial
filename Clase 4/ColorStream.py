import cv2

cam = cv2.VideoCapture(0)

while True:

    ret, frame = cam.read()

    frame = cv2.flip(frame, 1)
    #Conversiones
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    print(ret)

    cv2.imshow("Video Original", frame)
    cv2.imshow('Video HSV', hsv)
    cv2.imshow('Video gray', gray)

    t = cv2.waitKey(1)
    if t == 27:
        break

cam.release()

cv2.destroyAllWindows()
