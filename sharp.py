import numpy as np
import cv2

originalImage=cv2.imread("Lena.png");
grayscaleImage = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)
edgeImageGrayscale=np.zeros((originalImage.shape[0], originalImage.shape[1],1),np.uint8)
for y in range(0, grayscaleImage.shape[0]-1):
    for x in range(0, grayscaleImage.shape[1]-1):
        i = abs(int(grayscaleImage[y,x])-int(grayscaleImage[y+1,x+1])*2+int(grayscaleImage[y,x]))
        edgeImageGrayscale[y,x]=i if i<=255 else grayscaleImage[y,x]
cv2.imshow("sharpGrayscale",edgeImageGrayscale)
cv2.waitKey(0)