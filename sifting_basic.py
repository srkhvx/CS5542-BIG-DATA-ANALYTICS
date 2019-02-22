import cv2
import matplotlib

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from scipy.misc import imread, imresize

#matplotlib inline

pd.set_option('display.max_rows', 10)

image_file = 'p1.png'

img = cv2.imread(image_file)
plt.imshow(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
# Create a SIFT Object
sift = cv2.xfeatures2d.SIFT_create()

# Get the Key Points from the 'gray' image, this returns a numpy array
kp = sift.detect(gray, None)

# Now we drawn the gray image and overlay the Key Points (kp)
img = cv2.drawKeypoints(gray, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Plot it to the screen, looks a little small
plt.imshow(img)

# Save the image to a file
cv2.imwrite('sift_keypoints.jpg', img)