import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('dataset_logistic.csv').values
#print(data)
N,d = data.shape
print("N = ",N,"   d = ",d)
x = data[:,0:d-1].reshape(-1,d-1)
y = data[:,d-1].reshape(-1,1)

plt.scatter(x[:10,0],x[:10,1],c= 'g',marker='o',edgecolors='none',label='cho vay')
plt.scatter(x[10:,0],x[10:,1],c= 'red',marker='s',edgecolors='none',label='từ chối')
plt.xlabel("Mức lương")
plt.ylabel("Kinh nghiệm(số năm làm việc)")
plt.title("Bảng phân bố giá trị")
plt.legend(loc=1)

x = np.hstack((np.ones((N,1)),x))
w = np.array([0.,0.1,0.1]).reshape(-1,1)
iter = 1500
cost = np.zeros((iter,1))
learning_rate = 0.01
def sigmoid(z):
    return 1/(1+np.exp(-z))
for i in range(iter):
    y_predict = sigmoid(np.dot(x,w))
    cost[i] = np.sum(np.multiply(y,np.log(y_predict))+np.multiply(1-y,np.log(1-y_predict)))
    w-= learning_rate * np.dot(x.T,y_predict - y)
    print(cost[i])
x_dic ={'luong':8,'kn':2}
y_rs = sigmoid(w[0] + x_dic['luong'] * w[1] + x_dic['kn'] * w[2])
print(f"Dự đoán người có lương {x_dic['luong']} tr và KN {x_dic['kn']} năm :")
print("cho vay" if y_rs >= 0.8 else "từ chối")

#vẽ đường phân cách :
x1 = (4,10)
def tim_x2(w,x) :
    t = 0.5
    rs = -(w[0] + w[1]*x + np.log((1/t)-1))/w[2]
    return rs
x2_dic ={'x21':tim_x2(w,x1[0]),'x22':tim_x2(w,x1[1])}
plt.plot(x1,(x2_dic['x21'],x2_dic['x22']),linestyle= '-',color='r')
plt.show()