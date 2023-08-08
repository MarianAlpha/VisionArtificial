import numpy as np
import cv2

cap = cv2.VideoCapture(0)

im1 = cv2.imread('frontal.jpg')
ancho = int(im1.shape[1]/5)
alto = int(im1.shape[0]/5)

im1 = cv2.resize(im1,(ancho,alto),interpolation=cv2.INTER_AREA)

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)

    #Buscamos puntos claves
    #Numero de puntos clave
    num_kpt = 500
    #Declaramos el objeto
    orb = cv2.ORB_create(num_kpt)
    keypoint1, descriptor1 = orb.detectAndCompute(gray_im1, None)
    keypoint2, descriptor2 = orb.detectAndCompute(gray_frame, None)

    #Dibujamos los puntos claves
    im1_display = cv2.drawKeypoints(im1, keypoint1, outImage=np.array([]), color=(255,0,0), flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    frame_display = cv2.drawKeypoints(frame, keypoint2, outImage=np.array([]), color=(255,0,0), flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)

    #mostramos las caracteristicas
    cv2.imshow("Captura", frame_display)
    cv2.imshow("Imagen", im1_display)

    t = cv2.waitKey(1)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()