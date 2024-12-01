import cv2
import numpy as np

img = cv2.resize(cv2.imread('frame.jpg'), (640,640))
kernel = np.array([[-4,-3,-2],[-1,0,1],[2,3,4]])
dst = cv2.filter2D(img, -1, kernel)
cv2.imshow('after',dst)
cv2.waitKey(0)
