import cv2


#Elegir la camara
cap = cv2.VideoCapture(0)

while True:

    #Leemos los fotogramas, ret es true cuando la video correcta este siendor realizada de manera correcta, de lo contrario false
    ret, frame = cap.read()

    frame = cv2.flip(frame,1)
    
    print(ret)

    #Mostrar los frames
    cv2.imshow('Video Capture',frame)

    #Cerrar la captura con el teclado, es 1 porque se lee el teclado cada 1ms
    t = cv2.waitKey(1)

    #t = 27, 27 es ESC en ascii
    if t == 27:
        break

# Se libera la videocaptura
cap.release()

#Cerrar la ventana
cv2.destroyAllWindows()