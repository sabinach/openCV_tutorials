#################
# IMPORTANT: RUN USING 'python2.7' NOT 'python' 
#################

import cv2

img = cv2.imread('mit_stata_center.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create sift object
sift = cv2.xfeatures2d.SIFT_create()
# keypoint attributes: (x,y), meaningful neighborhood, angle, strength, etc.
(keypoints, descriptors) = sift.detectAndCompute(gray, None) # img, mask

# debug
print('# keypoints: {}, descriptors: {}'.format(len(keypoints),
                                                descriptors.shape))

# [flags] 0: kp + grayscale, 1: kp + color, etc.
flag = 2
#flag = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS # draws kp size + orient)

# draw keypoints on image: src, keypoints, output, flags
cv2.drawKeypoints(gray, keypoints, img, flags=flag)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

