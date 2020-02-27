import numpy as np
import cv2

originalImage=cv2.imread("Lena.png");
#grayscale image
grayscaleImage = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("original image",originalImage)
cv2.imshow("grayscale image", grayscaleImage)

#threshhold 180

#binary grayscale
binarymageGrayscale=np.zeros((grayscaleImage.shape[0], grayscaleImage.shape[1],1),np.uint8)
for y in range(1, grayscaleImage.shape[0]):
    for x in range(1,grayscaleImage.shape[1]):
     binarymageGrayscale[y,x]=0 if grayscaleImage[y,x]<180 else 255
cv2.imshow("BinaryGrayscale threshhold 180", binarymageGrayscale)


cv2.waitKey(0)