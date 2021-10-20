import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dt = pd.read_csv('data_linear.csv',header=None).values
#print(dt)
N = dt.shape[0]
x = dt[:,0].reshape(-1,1)  #diện tích : chuyển về mt 2D
y = dt[:,1].reshape(-1,1)  #giá bán
print(x)
plt.scatter(x,y)
plt.xlabel("m2")
plt.ylabel("giá bán")
plt.title("Biểu đồ giá bán, m2")
#plt.show()
x = np.hstack((np.ones((N,1) ), x ))
w = np.array([0.,1.]).reshape(-1,1)  #wo = 0 , w1 = 1 Khởi tạo ban đầu.
learning_rate = 0.000001
iter = 100
MSE = np.zeros((iter,1))
for i in range(iter):
    r = np.dot(x,w) - y
    MSE[i] = 0.5 * np.sum(r*r)
    w[0] -= learning_rate * np.sum(r)
    w[1] -= learning_rate * np.sum(np.multiply(r,x[:,1].reshape(-1,1)))
    print(MSE[i])
predict = np.dot(x,w)
plt.plot((x[0][1],x[N-1][1]),(predict[0],predict[N-1]),'r')
plt.show()
x_new = 50
rs = w[0] + x_new * w[1]
print("Gia nha 50m2 : ",rs)
#np.save('weight.npy',w)
