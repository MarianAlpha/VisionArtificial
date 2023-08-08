import	cv2

cam = cv2.VideoCapture(0)

ancho = int(cam.get(3)) # 3 ancho, 4 alto
alto = int(cam.get(4)) 

print(ancho, alto)

# comandoi: cv2.VideoWriter(Nombre, Codificacion, FPS, Dimensiones)

out = cv2.VideoWriter('Video.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10,(ancho, alto))

while True:

    ret, frame = cam.read()

    frame = cv2.flip(frame, 1)
    #Guardar el video
    out.write(frame)

    cv2.imshow('Video Capture',frame)

    t = cv2.waitKey(1)
    if t == 27:
        break

cam.release()

cv2.destroyAllWindows()