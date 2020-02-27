import numpy as np
import cv2

originalImage=cv2.imread("Lena.png");
#grayscale image
grayscaleImage = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original Grayscale",grayscaleImage)
cv2.imshow("Original",originalImage)

#flip grayscale image
flipImageGrayscale=np.zeros((originalImage.shape[0], originalImage.shape[1],1),np.uint8)
width=grayscaleImage.shape[1]
for y in range(1, grayscaleImage.shape[0]):
    for x in range(1, grayscaleImage.shape[1]):
        flipImageGrayscale[y,x]=grayscaleImage[y,width-x]

cv2.imshow("flipGrayscale",flipImageGrayscale)


#flip BGR image
flipImageBGR=np.zeros((originalImage.shape[0], originalImage.shape[1],3),np.uint8)
width=originalImage.shape[1]
for i in range(0,originalImage.shape[2]):
    for y in range(1, originalImage.shape[0]):
        for x in range(1, originalImage.shape[1]):
            flipImageBGR[y,x,i]=originalImage[y,width-x,i]

cv2.imshow("flipBGR",flipImageBGR)

#RGB image
ImageRGB=np.zeros((originalImage.shape[0], originalImage.shape[1],3),np.uint8)
for i in range(0,originalImage.shape[2]):
    for y in range(1, originalImage.shape[0]):
        for x in range(1, originalImage.shape[1]):
            ImageRGB[y,x,i]=originalImage[y,x,2-i]

cv2.imshow("RGB", ImageRGB)

#flip RGB image
flipImageRGB=np.zeros((originalImage.shape[0], originalImage.shape[1],3),np.uint8)
width=originalImage.shape[1]
for i in range(0,originalImage.shape[2]):
    for y in range(1, originalImage.shape[0]):
        for x in range(1, originalImage.shape[1]):
            flipImageBGR[y,x,i]=originalImage[y,width-x,2-i]

cv2.imshow("flipRGB",flipImageBGR)
##according to this we can say channle R has more effcet than channel Blue (thers is more red in original picture)

cv2.waitKey(0)