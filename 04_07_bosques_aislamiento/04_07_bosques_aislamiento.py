import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv('empleados.csv', delimiter=";")

print(df.head())