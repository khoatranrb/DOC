import cv2
import numpy as np
from scipy.ndimage import convolve

#----------"Preprocessing"------------
img = cv2.imread("link",0)
img = cv2.resize(img, (200,200))
img = img[5:295,5:295]

m1 = [1 for i in range(9)]
m2 = [0 for i in range(56)]
m = [1 for i in range(121)]
m[:56], m[65:] = m2, m2
k = np.asanyarray(m).reshape((11,11))/9
#--------------------------------------

#--------------Before pading--------------------
before = convolve(img,k, mode='constant')[10:191,10:191]
#-----------------------------------------------

#---------------After padding-------------------
after = convolve(img,k, mode='constant')
# after = convolve(img,k, mode='reflect')
# after = convolve(img,k, mode='nearest')
# after = convolve(img,k, mode='wrap')

#-----------------------------------------------


cv2.imshow("", before)
cv2.imshow(".", after)
cv2.waitKey(0)
cv2.destroyAllWindows()
