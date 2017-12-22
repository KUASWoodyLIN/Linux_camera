import numpy as np
import cv2

PATH = '/home/woodylin/picture/'
WIDTH = 1280
HEIGHT = 720

cv2.namedWindow("left")
cv2.namedWindow("right")
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
# (1280, 720) (1920, 1080)
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter(PATH + 'left.avi', fourcc, 20.0, (WIDTH, HEIGHT))
out2 = cv2.VideoWriter(PATH + 'right.avi', fourcc, 20.0, (WIDTH, HEIGHT))


while cap1.isOpened() and cap2.isOpened():
    # Capture frame-by-frame
    _, left = cap1.read()
    _, right = cap2.read()

    # write the flipped frame
    out1.write(left)
    out2.write(right)

    cv2.imshow('left', left)
    cv2.imshow('right', right)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap1.release()
cap2.release()
out1.release()
out2.release()
cv2.destroyAllWindows()
