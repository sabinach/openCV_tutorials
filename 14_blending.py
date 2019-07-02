import numpy as np
import cv2

# openCV does math!
x = np.uint8([250])
y = np.uint8([10])

print('cv2 add: {}'.format(cv2.add(x,y))) # 250+10=260 -> 255
print('regular add: {}'.format(x+y)) # 250+10=260%256 -> 4


# CANNOT BLEND IMAGES OF DIFFERENT SIZES
# blend images
img1 = cv2.imread('scenic_background.jpg')
img2 = cv2.imread('tweety_bird.jpg')

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()



