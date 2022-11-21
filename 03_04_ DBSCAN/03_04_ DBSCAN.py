import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN


df = pd.read_csv('datos.csv', delimiter=";")
print(df.head())

dbscan = DBSCAN()
dbscan.fit(df)
labels = dbscan.labels_

print(labels)

plt.scatter(df['Variable1'],df['Variable2'], c=labels, cmap= "plasma")