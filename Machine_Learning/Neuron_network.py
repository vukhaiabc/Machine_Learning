import numpy as np
import pandas as pd

data = pd.read_csv('dataset_neuronNetwork.csv').values
N, d = data.shape
X = data[:, 0:d-1].reshape(-1, d-1)
y = data[:,-1].reshape(-1,1)

layers = [X.shape[1],2,1]
def sigmoid(x):
    return 1/(1+np.exp(-x))
def DH_sigmoid(s):
    return s * (1-s)

class Neuron_Network():
    def __init__(self,layers,learning_rate = 0.01): #layers = [2,2,2]
        self.layers = layers
        self.alpha = learning_rate
        self.W=[]
        self.b=[]
        for i in range(len(layers)-1):
            w_ = np.random.randn(layers[i],layers[i+1])
            b_ = np.zeros((layers[i+1],1))
            self.W.append(w_/layers[i])
            self.b.append(b_)
    def __str__(self):
        return f"Mô hình Neuron_Network [{self.layers}]"
    def fit_prepare(self,x,y):
        a = [x]  # mang 3 chieu

        out = a[-1] #lay gia tri dau vao la x
        n = len(self.layers)
        #Qua trinh feedforward
        for i in range(n-1):
            out = sigmoid(np.dot(out, self.W[i])+(self.b[i].T))
            a.append(out)

        #qua trinh backpropagation
        dA = [-(y/a[-1] - (1-y)/(1 - a[-1]))] #dao ham ham loi / d_kq
        dw = []
        db = []
        for i in range(n-2,-1,-1):
            dw_ = np.dot(a[i].T,dA[-1] * DH_sigmoid(a[i+1]))
            dA_ = np.dot(dA[-1] * DH_sigmoid(a[i+1]),self.W[i].T)
            db_ = np.sum(dA[-1] * DH_sigmoid(a[i+1]), 0).reshape(-1,1)
            dw.append(dw_)
            dA.append(dA_)
            db.append(db_)

        #dao nguoc dw,db
        dw = dw[::-1]
        db = db[::-1]

        #gradient descent :
        for i in range(0,n-1):
            self.W[i] = self.W[i] - self.alpha * dw[i]
            self.b[i] = self.b[i] - self.alpha * db[i]

    def fit(self, x,y,epochs = 20,verbose = 10):
        for epoch in range(0,epochs):
            self.fit_prepare(x,y)
            if epoch % verbose ==0 :
                loss = self.calc_loss(x,y)
                print(f" Epoch {epoch},loss = {loss}")
    def predict(self,x):
        for i in range(0,len(self.layers)-1):
            x = sigmoid(np.dot(x,self.W[i]) + self.b[i].T)
        return x
    def calc_loss(self,x,y):
        y_predict = self.predict(x)
        return -(np.sum(y*np.log(y_predict) + (1-y)*np.log(1-y_predict)))

nn = Neuron_Network(layers,0.1)
nn.fit(X,y,10000,100)
print("du doan x =[[5,2]] : ",nn.predict(np.array([[4,1]])))


