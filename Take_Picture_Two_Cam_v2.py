import os
import time
import numpy as np
import cv2

PATH = '/home/woodylin/picture/'

cv2.namedWindow("left")
cv2.namedWindow("right")
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

counter = 0
if cap1.isOpened() and cap2.isOpened():
  while True:
    _, left_frame = cap1.read()
    _, right_frame = cap2.read()

    cv2.imshow('left', left_frame)
    cv2.imshow('right', right_frame)
    keycode = cv2.waitKey(1)
    if keycode & 0xFF == ord('q'):
      break
    elif keycode & 0xFF == ord('t'):
      t = time.localtime()
      DIR = str(t.tm_year) + '_' + str(t.tm_mon) + '_' + str(t.tm_mday) + '_' + \
            str(t.tm_hour) + ':' + str(t.tm_min) + ':' + str(t.tm_sec) + '/'
      os.makedirs(PATH + DIR)
      cv2.imwrite(PATH + DIR + 'left_image.png', left_frame)
      cv2.imwrite(PATH + DIR + 'right_image.png', right_frame)
else:
  print "Camera 1 is :" + str(cap1.isOpened()) + "\tCamera 2 is :" + str(cap2.isOpened())

# When everything done, release the capture
cap1.release()
cap2.release()
cv2.destroyAllWindows()