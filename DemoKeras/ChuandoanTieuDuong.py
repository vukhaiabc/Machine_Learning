import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import load_model

dataset = np.loadtxt('pima-indians-diabetes.data.csv',delimiter=',')
x = dataset[:,0:8]
y = dataset[:,8]
x_train_val,x_test,y_train_val,y_test= train_test_split(x,y,test_size=0.1)
x_train,x_val,y_train,y_val= train_test_split(x_train_val,y_train_val,test_size=0.2)

#build model
model = Sequential()
model.add(Dense(16,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(4,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=100,batch_size=5,validation_data=(x_val,y_val))

#load model
#model = load_model('mymodel1.h5')

#test
x_new = np.expand_dims(x_test[5],axis=0)
y_new = y_test[5]
y_predict = model.predict(x_new)
print("KQ : ",y_predict)
print("Thuc Te :",y_new)