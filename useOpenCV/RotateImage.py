import cv2
import imutils
image = cv2.imread("QK_rs.jpg",1)
cv2.imshow("quang khai",image)
cv2.waitKey(1000)

image_rotate = imutils.rotate(image,-45)
cv2.imshow("quang khai quay",image_rotate)
cv2.waitKey()
cv2.destroyAllWindows()