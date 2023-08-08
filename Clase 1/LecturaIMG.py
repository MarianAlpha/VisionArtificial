import cv2
import matplotlib.pyplot as plt

#Leer imagen

#Leer en gris
imggray = cv2.imread("img.jpg", 0) # 1 canal

#Leer a color RGB
imgRGB = cv2.imread("img.jpg", 1) # 3 canales

#Leer 
img = cv2.imread("img.jpg") # Por defecto a color BGR

#Extarer atributos gris
tama = imggray.shape
tipo = imggray.dtype

print("Tamaño Gray | Tipo de dato | ",tama,tipo)

#Extarer atributos color
tamaRGB = imgRGB.shape
tipoRGB = imgRGB.dtype

print("Tamaño RGB | Tipo de dato | ",tamaRGB,tipoRGB)


#Mostrar imagen

cv2.imshow("Gray", imggray)
cv2.imshow("RGB", imgRGB)
cv2.imshow("Img", img)

#Si no se muestra con cv2 si no con plt, se va a mostrar en GBR, cv2 hace la correccion automatica, aqui hay que hacerla a mano

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()

#Con el teclado pasamos la imagen
cv2.waitKey(0)