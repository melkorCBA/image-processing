import numpy as np
import cv2
import matplotlib.pyplot as plt

originalImage=cv2.imread("Lena.png");
#grayscale image
grayscaleImage = cv2.imread("Lena.png", cv2.IMREAD_GRAYSCALE)

#histrogram for grayscale

valuesGray=[]
for y in range(1, grayscaleImage.shape[0]):
    for x in range(1, grayscaleImage.shape[1]):
        valuesGray.append(grayscaleImage[y,x])


plt.hist(valuesGray, bins=range(256), color='black', label="GrayScale");
plt.show()

#acording to the histogram gray levels are between 35 - 240, /level 59.6 has the heihest frequency

#colour histogram
valuesColour=[]
valuesColour.append([])
valuesColour.append([])
valuesColour.append([])

for y in range(1, originalImage.shape[0]):
    for x in range(1, originalImage.shape[1]):
        valuesColour[0].append(originalImage[y, x, 0])
        valuesColour[1].append(originalImage[y, x, 1])
        valuesColour[2].append(originalImage[y, x, 2])

colour=['b', 'g', 'r']
for j in range(3):
    plt.hist(valuesColour[j], bins=range(256), color=colour[j]);
plt.show()


cv2.waitKey(0)