from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs  
from matplotlib import pyplot as plt 

clusters = [[6,6,6], [2,2,2], [3,9,9]]
X, y = make_blobs(centers = clusters, cluster_std = 0.70)