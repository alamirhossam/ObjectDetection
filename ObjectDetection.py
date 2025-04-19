#By Alamir Hossam 120210301
#Salma Amin 120210389

import cv2
import numpy as np

# Load query image (grayscale)
query_img = cv2.imread('query.jpg', cv2.IMREAD_GRAYSCALE)

# Load target image in both grayscale (for matching) and color (for drawing)
target_gray = cv2.imread('target.jpg', cv2.IMREAD_GRAYSCALE)
target_color = cv2.imread('target.jpg')  # For final output with rectangle

# Check if images loaded successfully
if query_img is None or target_gray is None or target_color is None:
    print("❌ Error: Make sure 'query.jpg' and 'target.jpg' are in the same folder as this script.")
    exit()

# Initialize SIFT detector
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(query_img, None)
kp2, des2 = sift.detectAndCompute(target_gray, None)

# Use FLANN matcher
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

# Lowe's ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

# Proceed only if we have enough good matches
if len(good_matches) > 10:
    # Extract match points
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # Find homography
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    # Get the corners of the query image
    h, w = query_img.shape
    query_corners = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
    target_corners = cv2.perspectiveTransform(query_corners, M)

    # Draw the rectangle on the color target image
    cv2.polylines(target_color, [np.int32(target_corners)], True, (0, 255, 0), 3, cv2.LINE_AA)

    # Show result
    cv2.imshow("Detected Object", target_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("❌ Not enough good matches were found - try a clearer image.")
