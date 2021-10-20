import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

my_df = pd.read_csv('dataset.csv')
x = my_df.values[:,2]
y = my_df.values[:,4]
"""plt.scatter(x,y,marker='o')
plt.show()"""
def result_sales(x_new , weight,bias):
    rs = weight*x_new + bias
    return rs
def cost_fun(x,y,w,b):
    n = len(x)
    sum_er = 0
    for i in range(n):
        sum_er += (y[i] - (x[i] * w + b))**2
    return sum_er/n
def update_weight(x,y,w,b,learning_rate):
    n = len(x)
    w_temp = 0.0
    b_temp = 0.0
    for i in range(n):
        w_temp += -2*x[i] *(y[i] - (x[i]*w + b))
        b_temp += -2 * (y[i] - (x[i]*w + b))
    w -=(w_temp / n) * learning_rate
    b -=(b_temp / n) * learning_rate

    return w,b
def train(x,y,w,b,learning_rate,iter):
    cost_his = []
    for i in range(iter):
        w,b = update_weight(x,y,w,b,learning_rate)
        cost = cost_fun(x,y,w,b)
        cost_his.append(cost)
    return w,b,cost_his
w,b,cos_his=train(x,y,0.03,0.0014,0.001,30)
print(w,"\t",b,"\t")
print("Du doan : ",result_sales(19,w,b))
plt.plot([i for i in range(30)],cos_his)
plt.show()
