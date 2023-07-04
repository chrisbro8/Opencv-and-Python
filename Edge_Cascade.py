import cv2 as cv

img=cv.imread('Photos/park.jpg')
cv.imshow('OriginalPicture',img)


# Edge Cascade -Finding the Edges in a frame
canny=cv.Canny(img,125,175)# nameread,thresholdvalue1,threshold value2
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
canny2=cv.Canny(blur,125,175)# Using Blur ina a cascade reduces the amount of edges in the picture
cv.imshow('Blurred',blur)
cv.imshow('Casacading1',canny) #preety cool
cv.imshow('Casacading2',canny2) #preety cool











cv.waitKey(0)