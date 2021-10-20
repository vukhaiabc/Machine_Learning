import cv2
import numpy as np
image = cv2.imread("QK_rs.jpg",1)
cv2.imshow("khai",image)
cv2.waitKey(1000)
kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])
#print(image[3:6,4:7])
print(image[5,6] * kernel)
print(kernel)
for i in range(1,597):
    for j in range(1,590):
        image[i][j] = np.dot((image[i][j]) ,kernel)
cv2.imshow("anh sau khi kernel ",image)
cv2.waitKey(0)
print(image.shape)
cv2.destroyAllWindows()