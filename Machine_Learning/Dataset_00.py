from sklearn.datasets import load_iris
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree

data_set = load_iris()
x_train,x_test,y_train,y_test = train_test_split(data_set.data,data_set.target,test_size=0.25)
model = tree.DecisionTreeClassifier()
rs_train = model.fit(x_train,y_train)
print("Độ chính xác : " , model.score(x_test,y_test))
x_new =x_test[2].reshape(1,4)
print(x_new)
y_pridict = rs_train.predict(x_new)
print("Dự đoán y = ", y_pridict)
print("Thực tế : ",y_test[2])


