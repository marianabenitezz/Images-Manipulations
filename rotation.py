import numpy as np
import cv2

image = cv2.imread("joseph.jpg")

h, w = image.shape[:2]

#cv2.imshow("Original", image)
#cv2.waitKey(0)

def rotation(degree, image):
	height = imagem.shape[0],
	width = imagem.shape[1]
    center = (width / 2, height / 2) #ponto no centro da figura
    rotation = cv2.getRotationMatrix2D(center, degree, 1.0)
    
    
    rotatedImage = cv2.warpAffine(image, rotation, (width, height))
    cv2.imshow("Rotacionado", rotatedImage)

    cv2.waitKey(0)



#Rotacionando 90° para esquerda
rotation(w, h, 90, image)

#Rotacionando 90° para direita
rotation(w, h, -90, image)