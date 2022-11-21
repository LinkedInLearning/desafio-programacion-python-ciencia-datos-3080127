import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import normalize
from sklearn.cluster import AgglomerativeClustering

df = pd.read_csv('clientes.csv', delimiter=";")

print(df.head())