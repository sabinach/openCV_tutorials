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

# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50) # or pass empty dictionary

# create flann matcher object
flann = cv2.FlannBasedMatcher(index_params, search_params)

# get the k best matches in two images
# matches objects have: distance, train descriptor index,
# query descriptor index, train image index
matches = flann.knnMatch(desc1, desc2, k=2)

# draw only good matches, so create mask
matchesMask = [[0,0] for i in xrange(len(matches))]

# apply ratio test
for i, (m,n) in enumerate(matches):
    if m.distance < 0.75*n.distance:
        matchesMask[i] = [1,0]

# drawing parameters
draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255, 0, 0),
                   matchesMask = matchesMask,
                   flags = 0)

# draw first 10 matches
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)

# show image
cv2.imshow('sift matches w/ flann matcher', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

