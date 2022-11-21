from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs  
from matplotlib import pyplot as plt 

clusters = [[6,6,6], [2,2,2]]
X, y = make_blobs(centers = clusters, cluster_std = 0.70)


bandwidth = estimate_bandwidth(X, n_samples=500)
meanshift = MeanShift(bandwidth=bandwidth)
meanshift.fit(X)
cluster_centers = meanshift.cluster_centers_


fig = plt.figure()
  
ax = fig.add_subplot(111, projection ='3d')
  
ax.scatter(X[:, 0], X[:, 1], marker ='.', color ="yellowgreen")
ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker ='o', color ='red', s=10, linewidth=5,  
                                   zorder=10)
plt.show()