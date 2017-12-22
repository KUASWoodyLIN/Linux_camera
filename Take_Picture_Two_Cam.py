import os
import numpy as np
import cv2

PATH = '/home/woodylin/picture/'

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

if cap1.isOpened() and cap2.isOpened():
  _, image1 = cap1.read()
  _, image2 = cap2.read()

  cv2.imwrite(PATH + 'image1.png', image1)
  cv2.imwrite(PATH + 'image2.png', image2)

  # When everything done, release the capture
  cap1.release()
  cap2.release()
  cv2.destroyAllWindows()

else:
  print "Camera 1 is :" + str(cap1.isOpened()) + "\tCamera 2 is :" + str(cap2.isOpened())

