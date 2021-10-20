import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,MaxPooling2D,Conv2D,Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
(x_train,y_train),(x_test,y_test)= mnist.load_data()

#chuyen doi kieu cua x,y
x_train = x_train.reshape(60000,28,28,1)
x_test = x_test.reshape(10000,28,28,1)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

#build model
model = Sequential()
model.add(Conv2D(64,kernel_size=(3,3),padding='same',input_shape=(28,28,1),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Conv2D(32,kernel_size=(3,3),padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Flatten())
model.add(Dense(10,activation='softmax'))

model.summary()
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=3,validation_data=(x_test,y_test))

y_predict = model.predict(x_test[2:3])
y_result = np.argmax(y_predict,axis=1)
print(y_result)
plt.imshow(x_test[2])
plt.show()
print(*y_result)

