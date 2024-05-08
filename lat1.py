import cv2
import numpy as np

# read gambar
img=cv2.imread('kucing.jpeg')
# operasi invers
im2= 255 - img
# menampilkan gambar
cv2.imshow('kucing.jpeg',im2)
cv2.waitKey(0)
cv2.destroyAllWindows()