import cv2
import numpy as np

def imprimeImagem(imagem):
    cv2.imshow("Imagens suavisadas (Blur)", imagem)
    cv2.waitKey(0)
    
def suaviza(img):
    img = img[::2,::2] # Diminui a imagem
    imgSuavizada = np.vstack([
     np.hstack([img, cv2.blur(img, ( 3, 3))]),
     #np.hstack([cv2.blur(img, (5,5)), cv2.blur(img, ( 7, 7))]),
     #np.hstack([cv2.blur(img, (9,9)), cv2.blur(img, (11, 11))]),
    ])
    imprimeImagem(imgSuavizada)

def suavizaPorFiltroGaussiano(img):
    img = img[::2,::2] # Diminui a imagem
    imgSuavizada = np.vstack([
        np.hstack([img, cv2.GaussianBlur(img, ( 3, 3), 0)]), 

        #np.hstack([cv2.GaussianBlur(img, ( 5, 5), 0), cv2.GaussianBlur(img, ( 7, 7), 0)]), 

        #np.hstack([cv2.GaussianBlur(img, ( 9, 9), 0), cv2.GaussianBlur(img, (11, 11), 0)]),
    ])
    imprimeImagem(imgSuavizada)

def suavizaPelaMediana(img):
    img = img[::2,::2] # Diminui a imagem
    imgSuavizada = np.vstack([
         np.hstack([img, cv2.medianBlur(img, 3)]),
         #np.hstack([cv2.medianBlur(img, 5), cv2.medianBlur(img, 7)]),
         #np.hstack([cv2.medianBlur(img, 9), cv2.medianBlur(img, 11)]),
     ])
    imprimeImagem(imgSuavizada)

def suavizaFiltroBilateral(img):
    img = img[::2,::2] # Diminui a imagem
    imgSuavizada = np.vstack([
         np.hstack([img, cv2.bilateralFilter(img, 3, 21, 21)]),
         #np.hstack([cv2.bilateralFilter(img, 5, 35, 35), cv2.bilateralFilter(img, 7, 49, 49)]),
         #np.hstack([cv2.bilateralFilter(img, 9, 63, 63), cv2.bilateralFilter(img, 11, 77, 77)])
     ])
    
    imprimeImagem(imgSuavizada)


img = cv2.imread('nomeImagem.jpg')