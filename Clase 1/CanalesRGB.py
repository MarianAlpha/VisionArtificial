import cv2
import matplotlib.pyplot as plt

#Se lee la imagen
img = cv2.imread("img.jpg")

#Corregimos
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

R = img[:,:,0]
B = img[:,:,1]
G = img[:,:,2]

#Otra opcion para sacar los canales

R,G,B = cv2.split(img)

print(img)

# Mostrar los canales

fig = plt.figure()

#Rojo
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(R, cmap="gray")
ax1.set_title("Canal Rojo")

#Verde
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(G, cmap="gray")
ax2.set_title("Canal Verde")

#Azul
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(B, cmap="gray")
ax3.set_title("Canal Azul")

#Reconstruimos la imagen porque separamos los canales
imgre = cv2.merge((R,G,B))

#Imagen Original
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(imgre)
ax4.set_title("Imagen Original")

plt.show()