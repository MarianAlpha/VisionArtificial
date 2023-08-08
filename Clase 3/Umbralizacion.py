import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('monedas.jpg')
imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

matriz = np.ones(gray.shape, dtype='uint8') * 50

# Umbralizacion imagen brillante
# Comando: retval, dst = cv2.threshold(img, thres(Umbra: debajo = 0, arriba = 255), maxval, tipo de umbral)
#          maxval = THRES_BINARY O THRES_BINARY_INV
# Comando: dst = cv2.adaptativeThreshold(img, maxValue, adaptativeMethod, thresholdType, blocksize)
#          thresholdType = THRES_BINARY O THRES_BINARY_INV

brillanteGray = cv2.add(gray, matriz)

_,imgthres1 = cv2.threshold(brillanteGray, 160, 255, cv2.THRESH_BINARY) #a partir de 160 hacia arriba poner todo en 255
_,imgthres2 = cv2.threshold(brillanteGray, 160, 255, cv2.THRESH_BINARY_INV)

imgadaptative = cv2.adaptiveThreshold(brillanteGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11,7) 

fig = plt.figure()

ax1 = fig.add_subplot(2,3,1)
ax1.imshow(imgrgb)
ax1.set_title('Imagen Original')

ax2 = fig.add_subplot(2,3,2)
ax2.imshow(brillanteGray, cmap="gray")
ax2.set_title('Imagen Brillante')

ax3 = fig.add_subplot(2,3,3)
ax3.imshow(imgthres1, cmap="gray")
ax3.set_title('Imagen threh 1')

ax4 = fig.add_subplot(2,3,4)
ax4.imshow(imgthres2, cmap='gray')
ax4.set_title('Imagen threh 2')

ax5 = fig.add_subplot(2,3,5)
ax5.imshow(imgadaptative, cmap='gray')
ax5.set_title('Imagen adaptativa')

plt.show()