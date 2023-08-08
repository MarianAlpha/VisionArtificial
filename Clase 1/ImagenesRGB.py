import cv2
import numpy as np
import matplotlib.pyplot as plt

#Crear la matriz principal
img = 100 * np.ones((10,10,3), np.uint8)

#Extaremos los canales

R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]

#Modificamos los canales

R[:,:] = 185
G[:,:] = 167
B[:,:] = 252

print(img)

plt.imshow(img)
plt.show()