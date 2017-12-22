import os
import numpy as np
import cv2

PATH = '/home/woodylin/picture/'

cap = cv2.VideoCapture(0)
# (1280, 720) (1920, 1080)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

if cap.isOpened():
  ret, frame = cap.read()

  cv2.imwrite(PATH + 'image.png', frame)

  # When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()

else:
  print "Can't found camera"

