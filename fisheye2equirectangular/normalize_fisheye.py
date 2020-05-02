import cv2
import numpy as np
import sys

center_x_offset = -24
center_y_offset = -27
radius_offset = 8

image = cv2.imread(sys.argv[1])
height, width = image.shape[0], image.shape[1]

center = (int(width/2) + center_x_offset, int(height/2) + center_y_offset)
radius = int(height/2) + radius_offset

left = max(center[0] - radius, 0)
top = max(center[1] - radius, 0)
right = min(center[0] + radius, width)
bottom = min(center[1] + radius, height)

crop = image[top:bottom, left:right, :]

left_offset = max(radius - center[0], 0)
top_offset = max(radius - center[1], 0)

nimage = np.zeros((radius * 2, radius * 2, 3), dtype='uint8')
nimage[top_offset:top_offset+crop.shape[0], left_offset:left_offset+crop.shape[1], :] = crop

cv2.imwrite(sys.argv[2], nimage)
