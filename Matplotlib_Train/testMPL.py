import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3]
y = [3,4,7]
plt.figure(figsize=(8,6))
plt.plot(x, y,linestyle='-',color='r',label='Doanh thu')
plt.plot([2,4,6], y,linestyle='--',color='yellow',label='Tăng Trưởng')
plt.xlabel("trục x")
plt.ylabel("trục y")
plt.title("Biểu đồ thống kê")
plt.legend(loc='best')
plt.show()