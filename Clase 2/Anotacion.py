import cv2

img = cv2.imread("dibujo.png")

#Redimensioamiento
img = red = cv2.resize(img,None, fx = 0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

#Linea
#Sintaxis img = cv2.line(imagen, pt1(x,y) inicio, pt2 final, color(B,G,R), grosor de la liena, tipo de linea)
linea = cv2.line(img, (int(1070/2), int(194/2)), (int(1152/2), int(467/2)), (255,0,0), thickness=2, lineType=cv2.LINE_AA)

#Circulo
#Sintaxis img = cv2.circle(imagen, pt1(x,y), radio, color, grosor, tipo linea
circulo = cv2.circle(img,(int(1080/2), int(185/2)), 70, (255,255,0), thickness=1, lineType=cv2.LINE_AA)

#Rectangulo
#Sintaxis img = cv2.rectangle(imagen, pt1, pt2, color, grosor, tipo)
rectaangulo = cv2.rectangle(img,(int(1010/2), int(425/2)), (int(1381/2), int(566/2)), (255,0,255),thickness=1,lineType=cv2.LINE_AA)

#Texto
#Sintaxis txt = cv2.puText(imagne, texto, pt1(sup-izq), fuente, size, color, grosor, tipo)
texto = 'Robot Detectado'
fuente = cv2.FONT_ITALIC
tam = 1.1
color = (0,255,0)
grosor = 2
text = cv2.putText(img, texto, (int(955/2), int(650/2)), fuente, tam, color, thickness=grosor)

#Mostrar
cv2.imshow('Imagen',img)
cv2.waitKey(0)