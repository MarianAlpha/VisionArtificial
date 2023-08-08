import cv2
import matplotlib.pyplot as plt
import numpy as np

img = 100*np.ones((10,10,3), np.uint8)
img2 = 100*np.ones((10,10,3), np.uint8)


#Se modifica el pixel 4,3 del R
img[4,5,0] = 255
img[4,4,0] = 0
img[5,4,0] = 255
img[5,5,0] = 0

#Se modifica el pixel 4,3 del G
img[4,5,1] = 0
img[4,4,1] = 255
img[5,4,1] = 0
img[5,5,1] = 255

#Se modifica el pixel 4,3 del B
img[4,5,2] = 255
img[4,4,2] = 255
img[5,4,2] = 0
img[5,5,2] = 0

#Recortar
recorte = img[3:7, 3:7]

#Mostrar el recorte
fig = plt.figure()

ax1 = fig.add_subplot(1,2,1)
ax1.imshow(img)
ax1.set_title("Imagen")

ax2 = fig.add_subplot(1,2,2)
ax2.imshow(recorte)
ax2.set_title("Recorte")

plt.show()

#Recortar una imagen
imagen = cv2.imread('img.png')

logo = imagen[168:222,256:328]

cv2.imshow('Imagen Original',imagen)
cv2.imshow('Imagen Recortada',logo)

cv2.waitKey(0)