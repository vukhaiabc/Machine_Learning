import cv2
img = cv2.imread("QK_rs.jpg",1)
cv2.imshow("anh ban dau",img)
cv2.waitKey(1000)
for i in range(300):
    for j in range(400):
        if(img[i,j,0] > 127) :
            img[i,j]=1
cv2.imshow("sau thay doi",img)
cv2.waitKey()
cv2.destroyAllWindows()