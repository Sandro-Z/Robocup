import cv2
img=cv2.imread('frame.jpg')
blockSize=2
ksize=3
k=0.04
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dst=cv2.cornerHarris(gray,blockSize,ksize,k)
print(dst)
img[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow('harris检测',img)
cv2.waitKey()