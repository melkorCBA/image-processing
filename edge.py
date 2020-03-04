import numpy as np
import cv2

originalImage=cv2.imread("Lena.png");
grayscaleImage = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)
edgeImageGrayscale=np.zeros((originalImage.shape[0], originalImage.shape[1],1),np.uint8)
for y in range(0, grayscaleImage.shape[0]-1):
    for x in range(0, grayscaleImage.shape[1]-1):
        i = int(grayscaleImage[y,x])-int(grayscaleImage[y,x+1])
        edgeImageGrayscale[y, x] =  0 #grayscaleImage[y,x]
        if(i>0):
            edgeImageGrayscale[y,x]=i*4 if i<255 else 0 #grayscaleImage[y,x]
cv2.imshow("edgeGrayscale",edgeImageGrayscale)
cv2.waitKey(0)