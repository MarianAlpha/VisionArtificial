import cv2
import numpy as np
import matplotlib.pyplot as plt

#imagen negra

img = np.zeros((10,10,1), np.uint8)

img[2,4] = 30
img[7,5] = 100
img[1,8] = 250
img[4,5] = 50


#Mostrar los valores numericos
print(img)

#Mostrar la imagen
plt.imshow(img, cmap='gray')
plt.show()