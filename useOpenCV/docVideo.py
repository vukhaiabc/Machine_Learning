import cv2
import imutils

camera_id = "C:\\Users\\Admin 88\\Pictures\\PKL.mp4"
cap = cv2.VideoCapture(camera_id)
rotate = 0
while True :
    ret,frame = cap.read()
    if ret:
        image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        image_rotate = imutils.rotate(image,rotate)
        cv2.imshow("Video PLK",image_rotate)
    key = cv2.waitKey(1)
    if key == ord('q'): break
    if key == ord('l'):
        rotate = 90
    if key == ord('r'):
        rotate = -90