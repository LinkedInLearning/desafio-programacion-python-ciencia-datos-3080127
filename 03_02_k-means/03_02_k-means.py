import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


df = pd.read_csv('clusters.csv', delimiter=";")
print(df.head(10))