import cv2
import numpy as np

img = cv2.imread('roi.jpg') # load color image
print('initial BGR: {}'.format(img[100,100])) # BGR pixel values

# accessing only blue pixel
blue = img[100, 100, 0]
print('blue pixel value: {}'.format(blue))
# another way: find RED
red = img.item(100, 100, 2)
print('red pixel value: {}'.format(red))

# modify pixel values 
img[100, 100] = [255, 255, 255] 
print('modified pixel values: {}'.format(img[100, 100]))
# another way: modify RED value
img.itemset((100, 100, 2), 100)
print('modified red: {}'.format(img.item(100, 100, 2)))

print('')

# image shape
print('image shape: {}'.format(img.shape))

# image size
print('image size: {}'.format(img.size))

# image datatype
print('image datatype: {}'.format(img.dtype))

'''
# copy one place to another 
ball = img[280:340, 330:390, 3]
img[273:333, 100:160, 3] = ball
'''

# show image
cv2.imshow('copied ball', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
