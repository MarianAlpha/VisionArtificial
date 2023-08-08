import cv2

img1 = cv2.imread('2.png')

#Redimencionar
img1 = cv2.resize(img1, None, fx = 0.5, fy = 0.5, interpolation=cv2.INTER_CUBIC)

circ1 = cv2.circle(img1, (int(421/2),int(1072/2)), int(392/2), (255,0,0), thickness=2, lineType=cv2.LINE_AA)
circ2 = cv2.circle(img1, (int(347/2), int(454/2)), int(60/2), (255, 0, 100),  thickness=1, lineType=cv2.LINE_AA)
circ3 = cv2.circle(img1, (int(498/2), int(448/2)), int(60/2), (255,0,100), thickness=1, lineType=cv2.LINE_AA)
cuad = cv2.rectangle(img1, (int(247/2), int(391/2)), (int(590/2), int(508/2)), (255,100,200), thickness=1, lineType=cv2.LINE_AA)
text = cv2.putText(img1, 'Comedero Legolas', (int(125/2), int(103/2)), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), thickness=2, lineType=cv2.LINE_AA)

cv2.imshow('Circulos', img1)
cv2.waitKey(0)