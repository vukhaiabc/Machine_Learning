import cv2

image_gray = cv2.imread("QK_rs.jpg",0)
cv2.imshow("anh xam",image_gray)
cv2.waitKey(1000)

image_edges = cv2.Canny(image_gray,100,200)
cv2.imshow("anh canh",image_edges)
cv2.waitKey()
cv2.destroyAllWindows()