import cv2
import numpy as np

# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)

# create a black image, a window, and bind the function to the window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    # show the image
    cv2.imshow('dbclk for circle, press ESC to quit', img)

    # cv2.waitKey() returns a 32 Bit integer value (might be dependent on the 
    # platform). The key input is in ASCII which is an 8 Bit integer value. 
    # So you only care about these 8 bits and want all other bits to be 0. 
    # This you can achieve with:
    if cv2.waitKey(20) & 0xFF == 27:    # exit w/ ESC key
        break

cv2.destroyAllWindows()
cv2.waitKey(1)
