import cv2
import imutils
image_gray = cv2.imread("QK_rs.jpg",0)
cv2.imshow("quang khai",image_gray)
cv2.waitKey()

ret,Threshold  = cv2.threshold(image_gray,127,255,cv2.THRESH_BINARY)
cv2.imshow("quang khai",Threshold)
cv2.waitKey()
cv2.destroyAllWindows()
