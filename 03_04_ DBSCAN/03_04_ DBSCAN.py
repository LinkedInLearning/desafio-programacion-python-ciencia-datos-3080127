import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

df = pd.read_csv('datos.csv', delimiter=";")

print(df.head())


