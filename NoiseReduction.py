import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('joseph.jpg', 0)
#img = cv.imread('2_2019_11_18_45_foto_frente_doc.jpeg',0)

def fastNlMeansDenoisingColored(img):
    dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

    final = np.hstack([np.hstack([np.hstack([img]), np.hstack([dst])])])

    cv2.imshow('FastNlMeansDenoisingColored', final)
    cv2.waitKey(0)
    
def thresholdAnd(img):
    # global thresholding
    #133 132.0
    ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    # Otsu's thresholding
    ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    # Otsu's thresholding after Gaussian filtering
    blur = cv.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    # plot all the images and their histograms
    images = [img, 0, th1,
              img, 0, th2,
              blur, 0, th3]
    titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
              'Original Noisy Image','Histogram',"Otsu's Thresholding",
              'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

    for i in range(3):
        plt.subplot(3,3,i*3+1), plt.imshow(images[i*3],'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+2), plt.hist(images[i*3].ravel(),256)
        plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+3), plt.imshow(images[i*3+2],'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])