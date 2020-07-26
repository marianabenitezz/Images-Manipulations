import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image.jpg',0)

def histogramEqualization(img):
    hist,bins = np.histogram(img.flatten(),256,[0,256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()

    #plt.plot(cdf_normalized, color = 'b')
    #plt.hist(img.flatten(),256,[0,256], color = 'r')
    #plt.xlim([0,256])
    #plt.legend(('cdf','histogram'), loc = 'upper left')
    #plt.show()

    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')

    img2 = cdf[img]

    equ = cv2.equalizeHist(img)
    res = np.hstack((img,equ)) #stacking images side-by-side
    cv2.imwrite('image_EqHis.png',res)


def histogramCLAHE(img):
    # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(img)

    cv2.imwrite('image_CLAHE.jpg',cl1)


def teste(img):
    img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
    img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
    hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
     
    cv2.imwrite('ImagemResultado.jpg',hist_equalization_result)