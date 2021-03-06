import cv2
import numpy as np

SHOWTIME = 2000 # Time to show images

img = cv2.imread('test_data/2.jpg',0)
kernel = np.ones((5,5),np.uint8)
# Erode thin lines
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow('Erode',erosion)
cv2.waitKey(SHOWTIME)
cv2.destroyAllWindows()
# Dilation thick lines
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow('Dilation',dilation)
cv2.waitKey(SHOWTIME)
cv2.destroyAllWindows()
# opening - erosion followed by dilation
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening',opening)
cv2.waitKey(SHOWTIME)
cv2.destroyAllWindows()
# Closing - Dilation followed by Erosion
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing',closing)
cv2.waitKey(SHOWTIME)
cv2.destroyAllWindows()
# Morhplogy gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('gradient',gradient)
cv2.waitKey(SHOWTIME)
cv2.destroyAllWindows()
#top hat -It is the difference between input image and Opening of the image
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('tophat',tophat)
cv2.waitKey(SHOWTIME)
cv2.destroyAllWindows()
#blackhat - It is the difference between the closing of the input image and input image.
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('Balchat',tophat)
cv2.waitKey(SHOWTIME)
cv2.destroyAllWindows()
