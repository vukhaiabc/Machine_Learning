import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

data_frame = pd.read_csv('kmean_dataset.csv')
data = data_frame.values
plt.scatter(data[:,0],data[:,1],s=50,c='g')
plt.title('Phân bố cụm')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')

km = KMeans(n_clusters=15)
km.fit(data)
centers = km.cluster_centers_
print(centers)
plt.scatter(centers[:,0],centers[:,1],s=100,c='r')
plt.show()