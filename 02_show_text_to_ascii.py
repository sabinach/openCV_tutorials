import cv2

img = cv2.imread('pupper.jpg')

while True:
    cv2.imshow('press ESC to quit', img)
    key = cv2.waitKey(33)   # wait 33 milliseconds

    if key == 27:   # esc key to stop
        break
    elif key == -1:   # normally returns -1, don't print this
        continue
    else:
        print(chr(key) + ': {}'.format(key))    # print "text: ascii"

