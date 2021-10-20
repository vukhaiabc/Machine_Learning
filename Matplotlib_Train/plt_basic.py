import matplotlib.pyplot as plt
import numpy as np
from math import pi

plt.plot([1,2,5,9])
plt.xlabel('phần tử thứ ')
plt.ylabel('Giá trị y')
plt.show()

t = np.arange(1,4,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()

x = np.linspace(-pi,pi,30,endpoint=True)
plt.plot(x,np.sin(x),'-')
plt.plot(x,np.cos(x),'--')
plt.show()