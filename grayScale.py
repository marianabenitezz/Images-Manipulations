#OpenCV
import numpy as np
import cv2

image = cv2.imread('joseph.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
#cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)
  
cv2.waitKey(0)
cv2.destroyAllWindows()


#MatplotLib

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open('joseph.jpg')

#plt.imshow(image)
#plt.savefig("joseph_RGB_matplot.png")

image = Image.open('joseph.jpg').convert("L") 
image = np.asarray(image)
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.savefig("joseph_matplot.png")


#MatplotLib Function

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

gray = rgb2gray(mpimg.imread('joseph.jpg'))    
plt.imshow(gray, cmap=plt.get_cmap('gray'))
plt.savefig("joseph_matplot_function.png")




#Pillow

from PIL import Image
import numpy as np

img = Image.open('joseph.jpg').convert('LA')
img.save('greyscale_Pillow.png')
img