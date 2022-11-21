import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


df = pd.read_csv('clusters.csv', delimiter=";")
print(df.head(10))

kmeans = KMeans(n_clusters=4)
kmeans.fit(df)
y_kmeans = kmeans.predict(df)
cluster_centers = kmeans.cluster_centers_

plt.scatter(df['Latitud'], df['Longitud'], c=y_kmeans, s=20)
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', s=200)
plt.xlabel('Latitud')
plt.ylabel('Longitud')