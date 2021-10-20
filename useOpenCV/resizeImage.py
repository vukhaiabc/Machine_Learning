import cv2
image = cv2.imread("quangkhai.jpg",1)
cv2.imshow("khai",image)
cv2.waitKey(1000)

image_rs = cv2.resize(image,dsize=None,fx=0.5,fy=0.5)
cv2.imshow("Anh RS",image_rs)
cv2.waitKey()
cv2.destroyAllWindows()