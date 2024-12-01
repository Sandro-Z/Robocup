import cv2 as cv
#转换灰度图
img = cv.imread('frame.jpg')
cv.imshow('Original Image',img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
#二值化
ret,image_thresh_binary=cv.threshold(gray,128,255,cv.THRESH_BINARY)
cv.imshow('cat_thresh_binary',image_thresh_binary)

cv.waitKey(0)
cv.destroyAllWindows()