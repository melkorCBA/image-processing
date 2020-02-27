import numpy as np
import cv2

originalImage=cv2.imread("Lena.png");
#grayscale image
grayscaleImage = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("original image",originalImage)
cv2.imshow("grayscale image", grayscaleImage)

#negitive imageGRB
negetiveImageGRB=np.zeros((originalImage.shape[0], originalImage.shape[1],3),np.uint8)
for y in range(1, originalImage.shape[0]):
    for x in range(1,originalImage.shape[1]):
     negetiveImageGRB[y,x]=255-originalImage[y,x];
cv2.imshow("Negetive GRB", negetiveImageGRB)

#negitive imageGrayscale
negetiveImageGrayscale=np.zeros((grayscaleImage.shape[0], grayscaleImage.shape[1],1),np.uint8)
for y in range(1, grayscaleImage.shape[0]):
    for x in range(1,grayscaleImage.shape[1]):
     negetiveImageGrayscale[y,x]=255-grayscaleImage[y,x];
cv2.imshow("Negetive Grayscale", negetiveImageGrayscale)

cv2.waitKey(0)