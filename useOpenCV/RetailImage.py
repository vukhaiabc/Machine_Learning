import cv2

img = cv2.imread("QK_rs.jpg",1)
cv2.imshow("qk",img)
cv2.waitKey()

img_sub = img[100: 400, 200: 500]
img_sub = img_sub[:,:,1]
cv2.imshow("qk",img_sub)
cv2.waitKey()
"""print(img.shape[0])
print(img.size)
print(img.dtype)"""
cv2.destroyAllWindows()