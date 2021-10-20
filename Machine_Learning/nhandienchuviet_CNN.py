import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
from tensorflow.keras.models import load_model,Sequential
from tensorflow.keras.datasets import mnist
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.python.keras import Sequential

(x_train_val,y_train_val),(x_test,y_test) = mnist.load_data()
x_train,x_val,y_train,y_val = train_test_split(x_train_val,y_train_val,test_size=0.2)

#chuyen doi kieu x,y
x_val = x_val.reshape(x_val.shape[0],28,28,1)
x_train = x_train.reshape(x_train.shape[0],28,28,1)
x_test = x_test.reshape(x_test.shape[0],28,28,1)

# y : onehot vector
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)
y_test = to_categorical(y_test)

#build model :
"""model: Sequential = Sequential()
model.add(Conv2D(32,kernel_size=(3,3),padding='same',activation='sigmoid',input_shape=(28,28,1)))
model.add(Conv2D(32,kernel_size=(3,3),activation='sigmoid',))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(100,activation='sigmoid'))
model.add(Dense(10,activation='softmax'))


#huan luyen:
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,validation_data=(x_val,y_val),epochs=5,verbose=1)
model.save('nhanchuviet.h5')"""
model = load_model('nhanchuviet.h5')
score = model.evaluate(x_test,y_test)
print(score)

# tesssst
x_new = x_test[1]
y_predict = model.predict(x_new.reshape(1,28,28,1))
plt.imshow(x_new.reshape(28,28))
y_predict = np.argmax(y_predict)
print(y_predict)
plt.show()