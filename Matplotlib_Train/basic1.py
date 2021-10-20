import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,9,30)
plt.plot(x,x,linestyle='--',color='red')
plt.plot(x,x+1,linestyle='-',color='green')
plt.plot(x,x+2,linestyle='-.',color='black')
plt.plot(x,x+4,linestyle=':',color='0')
plt.show()