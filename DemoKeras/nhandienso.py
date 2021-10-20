import numpy as np
from keras.datasets import mnist
from tensorflow.keras.layers import Conv2D,Dense,MaxPooling2D,Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
from tensorflow.python.keras.models import load_model

(x_train,y_train),(x_test,y_test) = mnist.load_data()
print(x_train.shape)
"""plt.imshow(x_train[1])
plt.show()"""

x_train = x_train.reshape(60000,28,28,1)
x_test = x_test.reshape(10000,28,28,1)
y_train = to_categorical(y_train) #chuyen ve MT [1 0 0 0 0 0 0 0 0 0]
y_test = to_categorical(y_test)
print(y_train[1])

#build model
"""model = Sequential()
model.add(Conv2D(64,kernel_size=(3,3),activation='relu',input_shape=(28,28,1),padding='same'))
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Conv2D(32,kernel_size=(3,3),activation='relu',padding='same'))
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Flatten())
model.add(Dense(10,activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=3,validation_data=(x_test,y_test))

model.save('modelNumber.h5')"""

model =load_model('modelNumber.h5')
y_predict = model.predict(x_test[0:1])
y_result = np.argmax(y_predict,axis=1)
print(y_result)
plt.imshow(x_test[0])
plt.show()