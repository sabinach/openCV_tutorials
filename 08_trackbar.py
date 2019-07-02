import cv2
import numpy as np

def do_nothing(x):
    pass

# create black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R', 'image', 0, 255, do_nothing)
cv2.createTrackbar('G', 'image', 0, 255, do_nothing)
cv2.createTrackbar('B', 'image', 0, 255, do_nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1: ON'
cv2.createTrackbar(switch, 'image', 0, 1, do_nothing)

while True:
    cv2.imshow('switch ON and drag, press ESC to quit', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27: # exit w/ ESC key
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0: # if switch off, keep image black
        img[:] = 0
    else: # else, use BGR colors from trackbars
        img[:] = [b, g, r]

cv2.destroyAllWindows()
cv2.waitKey(1)


