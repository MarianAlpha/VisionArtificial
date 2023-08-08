import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("monedas.jpg")
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

matriz = np.ones(gray.shape, dtype='uint8') * 50
matrizRGB = np.ones(img.shape, dtype='uint8') * 550

#Aumentamos el brillo
brillanteRGB = cv2.add(img, matrizRGB)
brillanteRGBm = cv2.cvtColor(brillanteRGB, cv2.COLOR_BGR2RGB)

#Disminuimos brillo
OscuroRGB = cv2.subtract(img, matrizRGB)
OscuroRGBm = cv2.cvtColor(OscuroRGB, cv2.COLOR_BGR2RGB)

#Aumentar brillo wb
brillanteGray = cv2.add(gray, matriz)

#Disminuir brillo
OscuroGray = cv2.subtract(gray, matriz)

#Mostrar
fig = plt.figure()

#Filas, columnas, posicion
ax1 = fig.add_subplot(2,3,1)
ax1.imshow(imgRGB)
ax1.set_title('Imagen Original')

ax2 = fig.add_subplot(2,3,4)
ax2.imshow(gray, cmap="gray")
ax2.set_title('Escala de grises')

ax3 = fig.add_subplot(2,3,2)
ax3.imshow(brillanteRGBm)
ax3.set_title('Brillante RGB')

ax4 = fig.add_subplot(2,3,3)
ax4.imshow(OscuroRGBm)
ax4.set_title("Oscuro RGB")

ax5 = fig.add_subplot(2,3,5)
ax5.imshow(brillanteGray, cmap='gray')
ax5.set_title('Brillante gris')

ax6 = fig.add_subplot(2,3,6)
ax6.imshow(OscuroGray, cmap='gray')
ax6.set_title('Oscuro gris')

plt.show()

cv2.imshow('IMAGEN BRILLANTE GRAY',brillanteGray)
cv2.imshow('IMAGEN OSCURA GRAY', OscuroGray)
cv2.imshow('IMAGEN BRILLANTE RGB', brillanteRGB)
cv2.imshow('IMAGEN OSCURA RGB',OscuroRGB)
cv2.waitKey(0)