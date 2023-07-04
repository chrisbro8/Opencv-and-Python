import cv2 as cv

img=cv.imread('Photos/park.jpg')
cv.imshow('Picture',img)

# Dialiating An Image:- i used 
canny=cv.Canny(img,125,175)
dilated=cv.dilate(canny,(3,3),iterations=1)
# cv.dilate(src,kernelSize(in rectangle),iterartions)
cv.imshow('Canny Images',canny)
cv.imshow('Dialeted Edges',dilated)


# Eroding:-This is used to regaina dialted image
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded_Images',eroded)


# ..Resize

resized=cv.resize (img,(500,700),interpolation=cv.INTER_LINEAR)

# 700 is the height and 500 is the width of the resized images
# img is the source 

'''Types of Interpolation:
>cv.INTER_ARER:This is the default interpolation set by the "resize" //useful when it smaller the original image dimension
>cv.INTER_LINEAR: Used when larger than the original image dimension
>cv.INTER_CUBIC: Used when larger but these is the slowest but with the mostv quality 
'''
cv.imshow('Resized',resized)


# .. Cropping
cropped=img[0:800,0:300]
cv.imshow('Cropped_image',cropped)

 






cv.waitKey(0)