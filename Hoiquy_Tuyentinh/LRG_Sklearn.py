import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

dt = pd.read_csv('data_linear.csv').values
x = dt[:,0].reshape(-1,1)
y = dt[:,1].reshape(-1,1)

plt.scatter(x,y)
plt.xlabel("m2")
plt.ylabel("Giá Nhà")
plt.title("Dự Đoán Giá Nhà")

lrg_model = LinearRegression() # tạo model
lrg_model.fit(x,y) #train
y_predict = lrg_model.predict(x)
plt.plot((x[0],x[-1]),(y_predict[0],y_predict[-1]),'g')
x_new = [[50]]
y_rs = lrg_model.predict(x_new)
print("Kết quả dự đoán nhà 50 m2 : ",*y_rs)
plt.show()
