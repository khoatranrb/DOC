import cv2
from scipy import ndimage
import numpy as np

img = cv2.imread('/home/khoatranrb/Desktop/hd88.jpg',0)

m1 = np.ones((3,3))/9

m2 = np.asanyarray([-1,-2,-1,-2,12,-2,-1,-2,-1]).reshape((3,3))/16

def conv(I,K):
    h, w = I.shape[:2]
    k = K.shape[0]
    res = np.zeros((h+k-1,w+k-1))
    d = int((k-1)/2)
    res[d:-d,d:-d] = I
    return ndimage.convolve(res,K,mode='constant')

m1 = m1.astype(np.float32)
m2 = m2.astype(np.float32)
img = img.astype(np.float32)

m3 = conv(m2,m1)

img1 = conv(img,m1)
img2 = conv(img,m2)
img3 = conv(img,m3)
img12 = conv(img1,m2)
img21 = conv(img2,m1)

def cvt(imgIn):
    img = imgIn.astype(np.uint8)
    img = np.where(img<0,0,img)
    img = np.where(img>255,255,img)
    return img

img1 = cvt(img1)
img2 = cvt(img2)
img3 = cvt(img3)
img12 = cvt(img12)
img21 = cvt(img21)

img = img.astype(np.uint8)

cv2.imshow('', img)
cv2.imshow('1', img1)
cv2.imshow('2', img2)
cv2.imshow('3', img3)
cv2.imshow('12', img12)
cv2.imshow('21', img21)
cv2.waitKey(0)
cv2.destroyAllWindows()
