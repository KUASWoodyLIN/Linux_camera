import numpy as np
import cv2

PATH = '/home/woodylin/picture/'
WIDTH = 1280
HEIGHT = 720

cap = cv2.VideoCapture(0)
# (1280, 720) (1920, 1080) (640, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(PATH + 'output.avi', fourcc, 20.0, (WIDTH, HEIGHT))

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()