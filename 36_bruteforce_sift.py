####################
# IMPORTANT: RUN USING 'python2.7' NOT 'python'
####################

import cv2

# GOOD
img1 = cv2.imread('cereal_frostedflakes.jpg', 0)
img2 = cv2.imread('cereal_frostedflakes_more.jpg',0)

# OKAY
#img1 = cv2.imread('cereal_honeybunches.png', 0)
#img2 = cv2.imread('cereal_brands.jpg', 0)

# BAD
#img1 = cv2.imread('cereal_frootloops.jpeg', 0)
#img2 = cv2.imread('cereal_brands.jpg', 0)

# initiate ORB detector
sift = cv2.xfeatures2d.SIFT_create()

# find keypoints nad descriptors with ORB
kp1, desc1 = sift.detectAndCompute(img1, None)
kp2, desc2 = sift.detectAndCompute(img2, None)

# create matcher object w/ default parameters
bf_matcher = cv2.BFMatcher()

# get the k best matches in two images
# matches objects have: distance, train descriptor index,
# query descriptor index, train image index
matches = bf_matcher.knnMatch(desc1, desc2, k=2)

# apply ratio test
good = []
for m, n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# draw first 10 matches
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

# show image
cv2.imshow('sift matches', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

