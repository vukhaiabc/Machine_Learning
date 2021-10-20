from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def kmeans_display(X, label,center=False):
    K = np.amax(label) + 1
    X0 = X[label == 0 , :]
    X1 = X[label == 1 , :]
    X2 = X[label == 2 , :]

    plt.plot(X0[: , 0],X0[:,1] ,'b^' , markersize = 6,alpha = .8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize=6, alpha=.8)
    plt.plot(X2[:, 0], X2[:, 1], 'ys', markersize=6, alpha=.8)
    plt.plot(center[:,0],center[:,1],'r*',markersize= 20 , alpha=.8)
    plt.title('Phân bố cụm')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.show()

np.random.seed(11)
means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(means[0],cov , N)
X1 = np.random.multivariate_normal(means[1],cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)
X = np.concatenate((X0,X1,X2),axis=0)
print(X.shape)

kmeans = KMeans(n_clusters=3,random_state=0).fit(X)
print(kmeans.cluster_centers_)
labels = kmeans.predict(X)
print(labels)

kmeans_display(X,labels,kmeans.cluster_centers_)