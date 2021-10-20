import numpy as np
import pandas as pd

data = pd.read_csv('dataset_neuronNetwork.csv').values
N,d  = data.shape
X = data[:,0:d-1].reshape(-1,d-1)
y = data[:,-1].reshape(-1,1)
layers = [X.shape[1],2,1]

def sigmoid(x):
    return 1/(1+np.exp(-x))
def dh_sigmoid(s):
    return s * (1-s)
class Neuron_NW():
    def __init__(self,layers,learning_rate = 0.01):
        self.layers = layers
        self.alpha = learning_rate
        self.W = []
        self.b = []

        for i in range(len(layers)-1):
            w_ = np.random.randn(layers[i],layers[i+1])
            b_ = np.zeros((layers[i+1],1))
            self.W.append(w_/layers[i])
            self.b.append(b_)
    def __str__(self):
        return f"Neuron_NW {self.layers}"
    def fit_prepare(self,x,y):
        A = [x] #mang 3 chieu
        n = len(self.layers)
        out = A[-1]
        for i in range(0,n-1):
            out = sigmoid(np.dot(out,self.W[i]) + self.b[i].T)
            A.append(out)

        #lan truyen nguoc
        dA = [-(y/A[-1] - (1-y)/(1-A[-1]))]  #A[-1] == ket qua cuoi
        dw = []
        db = []
        for i in range(n-2,-1,-1):
            dw_ = np.dot(A[i].T,dA[-1] * dh_sigmoid(A[i+1]))
            dA_ = np.dot(dA[-1] *dh_sigmoid(A[i+1]), self.W[i].T)
            db_ = np.sum(dA[-1] *dh_sigmoid(A[i+1]),0).reshape(-1,1)
            dA.append(dA_)
            db.append(db_)
            dw.append(dw_)

        #dao nguoc dw,db
        dw = dw[::-1]
        db = db[::-1]
        for i in range(0,n-1):
            self.W[i] = self.W[i] - self.alpha * dw[i]
            self.b[i] = self.b[i] - self.alpha * db[i]
    def predict(self,x):
        for i in range(0,len(self.layers)-1):
            x = sigmoid(np.dot(x, self.W[i]) + self.b[i].T)
        return x
    def calc_loss(self,x,y):
        y_predict = self.predict(x)
        loss = -(np.sum((y * np.log(y_predict) + (1-y) * np.log(1 - y_predict))))
        return loss
    def fit(self,x,y,epochs= 20, verbose = 10):
        for epoch in range(0,epochs):
            self.fit_prepare(x,y)
            if epoch % verbose ==0:
                loss = self.calc_loss(x,y)
                print(f"Epoch {epoch} , loss = {loss}")
nn = Neuron_NW(layers,0.1)
nn.fit(X,y,10000,100)
print("Du doan [9,0.5] : ",nn.predict(np.array([[8,0.1]])))
