import cv2

imagen = cv2.imread("img.png")

#Redimensionar
# Sintaxis red = cv2.resize(imagen, fx=factor en x, fy=factor en y, tipo de interpolacion)

#Red 1
red1 = cv2.resize(imagen, None, fx=1.5, fy=1.5)

#Red 2
red2 = cv2.resize(imagen, None, fx=1.5, fy=1.5, interpolation= cv2.INTER_AREA)

#Red 3
red3 = cv2.resize(imagen, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

#Red 4
ancho = 400
alto = 500
tam = (ancho,alto)
red4 = cv2.resize(imagen, tam, interpolation=cv2.INTER_CUBIC)

#Mostramos el recorte
cv2.imshow('Imagen original', imagen)
cv2.imshow('Redimension 1', red1)
cv2.imshow('Redimension 2', red2)
cv2.imshow('Redimension 3', red3)
cv2.imshow('Redimension 4', red4)

cv2.waitKey(0)
