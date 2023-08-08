import cv2

img = cv2.imread("img.png")

#Rotar 1 (arriba hacia abajo, una horizontal)
rot1 = cv2.flip(img,0)

#Rotar 2 Izquerda a derecha, vertical
rot2 = cv2.flip(img,1)

#Rotar 3 las dos juntas vertical y horizaontal
rot3 = cv2.flip(img,-1)

cv2.imshow('Original', img)
cv2.imshow('Rotacion 1', rot1)
cv2.imshow('Rotacion 2', rot2)
cv2.imshow('Rotacion 3', rot3)

cv2.waitKey(0)
