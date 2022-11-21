import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import normalize
from sklearn.cluster import AgglomerativeClustering

df = pd.read_csv('clientes.csv', delimiter=";")

print(df.head())

dendrogram(linkage(df, method='ward',  metric='euclidean'))
plt.axhline(y=15000, color='r', linestyle='--')

agglomerative = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
agglomerative.fit(df)
labels = agglomerative.labels_

print(labels)

plt.scatter(df['Salario'], df['Gasto'], c=labels) 
plt.xlabel('Salario Mensual')
plt.ylabel('Porcentaje Gasto Mensual')