import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data_linear.csv',header=None).values
x = data[:,0].reshape(-1,1)
y = data[:,1].reshape(-1,1)

N = data.shape[0]
plt.scatter(x,y)
plt.xlabel("m2")
plt.ylabel("Giá Bán")
plt.title("Giá nhà đất")
x = np.hstack((np.ones((len(x),1)),x))
w = np.array([0.,1.]).reshape(-1,1)
iter = 100
mse = np.zeros((iter,1))
learning_rate = 0.000001
for i in range(iter):
    r = np.dot(x,w) - y #gia tri dao ham
    mse[i] = 0.5 * sum(r*r)
    w[0] -= learning_rate * np.sum(r)
    w[1] -= learning_rate * np.sum(np.multiply(x[:,1].reshape(-1,1),r))
    print(mse[i])
pre = np.dot(x,w)
plt.plot((x[0][1],x[N-1][1]),(pre[0],pre[N-1]),'r')
plt.show()