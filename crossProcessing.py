import numpy as np
import cv2

originalImage=cv2.imread("Lena.png");
cv2.imshow("OriginalBGR",originalImage) #BGR image

#RGB image crossProcessing /B and R crossProcessing
ImageRGB=np.zeros((originalImage.shape[0], originalImage.shape[1],3),np.uint8)
for i in range(0,originalImage.shape[2]):
    for y in range(1, originalImage.shape[0]):
        for x in range(1, originalImage.shape[1]):
            ImageRGB[y,x,i]=originalImage[y,x,2-i]

cv2.imshow("RGB", ImageRGB)

#B and G crossProcessing
ImageGBR=np.zeros((originalImage.shape[0], originalImage.shape[1],3),np.uint8)
for i in range(0,originalImage.shape[2]):
    for y in range(1, originalImage.shape[0]):
        for x in range(1, originalImage.shape[1]):
            if(i==2):
                ImageGBR[y, x, i]=originalImage[y,x,i]
            else:
                ImageGBR[y,x,i]=originalImage[y,x,1-i]

cv2.imshow("GBR", ImageGBR)

#G and R crossProcessing
ImageBRG=np.zeros((originalImage.shape[0], originalImage.shape[1],3),np.uint8)
for i in range(0,originalImage.shape[2]):
    for y in range(1, originalImage.shape[0]):
        for x in range(1, originalImage.shape[1]):
            if(i==0):
                ImageBRG[y, x, i]=originalImage[y,x,i]
            else:
                ImageBRG[y,x,i]=originalImage[y,x,3-i]

cv2.imshow("BRG",ImageBRG)

cv2.waitKey(0)