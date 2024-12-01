import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('frame.jpg',0)
img_float = np.float32(img)
dft = cv2.dft(img_float,flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
rows,cols = img.shape
crow,col = int(rows/2), int(cols/2)
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30, col-30:col+30] = 255
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('input img'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title('fft img'), plt.xticks([]), plt.yticks([])
plt.show()


img = cv2.imread('frame.jpg',0)
img_float = np.float32(img)
dft = cv2.dft(img_float,flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
rows,cols = img.shape
crow,col = int(rows/2), int(cols/2)
mask = np.ones((rows,cols,2),np.uint8)
mask[crow-10:crow+10, col-10:col+10] = 0
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('input img'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title('fft img'), plt.xticks([]), plt.yticks([])
plt.show()