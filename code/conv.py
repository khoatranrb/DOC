import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

# Load ảnh
img = cv2.imread('đường dẫn ảnh',0)

# Khởi tạo ma trận bộ lọc
kernel = np.asanyarray([-1,0,1,-2,0,2,-1,0,1]).reshape((3,3))

corr = cv2.filter2D(img,-1, kernel)

# Chuyển ma trận ảnh về kiểu dữ liệu float
imgFloat = img.astype(float)
# Thực hiện convolution
conv = ndimage.convolve(imgFloat,kernel)
# Với output pixel < 0, đưa về giá trị 0
conv = np.where(conv<0, 0, conv)
# Với output pixel > 255, đưa về giá trị 255
conv = np.where(conv>255, 255, conv)
# Đưa ma trận về kiểu dữ liệu ban đầu
conv = conv.astype(np.uint8)

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(corr, cmap='gray')
plt.title('Cross-correlation')
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(conv, cmap='gray')
plt.title('Convolution')
plt.axis('off')

plt.show()
