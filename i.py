import cv2
import utils
import filters

img = utils.read_image()
img = filters.high_contrast(img)
cv2.imshow('image',img)
cv2.waitKey(0)
