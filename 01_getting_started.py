import numpy as np
import cv2

# read image
img = cv2.imread('pupper.jpg',0)

# show image
cv2.imshow('pupper',img)
k = cv2.waitKey(0)  # wait indefinitely
if k == 27:
    cv2.destroyAllWindows() # wait for ESC key to exit
elif k == ord('s'):
    cv2.imwrite('save_pupper_s.png',img)    # wait for 's' key to save
    cv2.destroyAllWindows()
    cv2.waitKey(1)

# save image
cv2.imwrite('save_pupper_esc.png',img)

# load window, then load image
# cv2.namedWindow()
# cv2.destroyWindow()
