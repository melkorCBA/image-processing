import numpy as np
import cv2

originalImage=cv2.imread("Lena.png");
#grayscale image
grayscaleImage = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)

#Brightness for grayscale
brightImageGray=np.zeros((grayscaleImage.shape[0], grayscaleImage.shape[1],1),np.uint8)
for y in range(1, grayscaleImage.shape[0]):
    for x in range(1, grayscaleImage.shape[1]):
        value=grayscaleImage[y,x]+100
        #fix-if totla is grater than 255 it will be 0
        if(value>256):
            brightImageGray[y,x] = 255
        else:
            brightImageGray[y, x]=value
cv2.imshow("Bright Grayscale", brightImageGray)

#Brightness for BGR
brightImageGRB=np.zeros((originalImage.shape[0], originalImage.shape[1],3),np.uint8)
for i in range(0, originalImage.shape[2]):
    for y in range(1,originalImage.shape[0]):
        for x in range(1, originalImage.shape[1]):
            value=originalImage[y,x,i]+100
            #fix-if totla is grater than 255 it will be 0
            if(value>256):
                brightImageGRB[y,x,i] = 255
            else:
                brightImageGRB[y, x,i]=value
cv2.imshow("Bright GRB", brightImageGRB)

#Brightness for B
brightImageB=np.zeros((originalImage.shape[0], originalImage.shape[1],3),np.uint8)
for y in range(1,originalImage.shape[0]):
    for x in range(1, originalImage.shape[1]):
        value=originalImage[y,x,0]+100
        #fix-if totla is grater than 255 it will be 0
        if(value>256):
            brightImageB[y,x,0] = 255
        else:
            brightImageB[y, x,0]=value
cv2.imshow("Bright B", brightImageB)

#Brightness for G
brightImageG=np.zeros((originalImage.shape[0], originalImage.shape[1],3),np.uint8)
for y in range(1,originalImage.shape[0]):
    for x in range(1, originalImage.shape[1]):
        value=originalImage[y,x,1]+100
        #fix-if totla is grater than 255 it will be 0
        if(value>256):
            brightImageG[y,x,1] = 255
        else:
            brightImageG[y, x,1]=value
cv2.imshow("Bright G", brightImageG)


#Brightness for R
brightImageR=np.zeros((originalImage.shape[0], originalImage.shape[1],3),np.uint8)
for y in range(1,originalImage.shape[0]):
    for x in range(1, originalImage.shape[1]):
        value=originalImage[y,x,2]+100
        #fix-if totla is grater than 255 it will be 0
        if(value>256):
            brightImageR[y,x,2] = 255
        else:
            brightImageR[y, x,2]=value
cv2.imshow("Bright R", brightImageR)

#acording to the BRG resutls increasing Green channel more Red less Blue mid  reveale more detail
#incerasing G channel by 150, B by 50 R by 0
brightImageGRB_1=np.zeros((originalImage.shape[0], originalImage.shape[1],3),np.uint8)
for i in range(0, originalImage.shape[2]):
    for y in range(1,originalImage.shape[0]):
        for x in range(1, originalImage.shape[1]):
            if(i==0): #Blue 50
                value = originalImage[y, x, i] + 50
            if(i==1):  #Green 150
                value=originalImage[y, x, i] + 150
            if(i==2):  #Red 0
                value=originalImage[y, x, i]

            #fix-if totla is grater than 255 it will be 0
            if(value>256):
                brightImageGRB_1[y,x,i] = 255
            else:
                brightImageGRB_1[y, x,i]=value
cv2.imshow("Bright GRB with more Green", brightImageGRB_1)



cv2.waitKey(0)