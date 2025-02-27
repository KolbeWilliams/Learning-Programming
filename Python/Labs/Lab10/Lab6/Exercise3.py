#Exercise 3: Change a given image with a user provided threshold
import cv2 #import openCV module/library
import numpy as np
img = cv2.imread('coinsGray.png', cv2.IMREAD_GRAYSCALE) #read grayscale image
img2 = img.copy()
#cv2.imshow('Gray scale image', img) #display image
cv2.waitKey(0) #hold screen until user closes it
cv2.destroyAllWindows() #close window

threshold = int(input(('Enter a threshold: ')))
for row in range(len(img2)):
    for column in range(len(img2[0])):
        if img2[row][column] > threshold:
            img2[row][column] = 255
        else:
            img[row][column] = 0
img = np.concatenate((img, img2), axis = 1)
cv2.imshow('Gray scale image', img)
cv2.waitKey(0)