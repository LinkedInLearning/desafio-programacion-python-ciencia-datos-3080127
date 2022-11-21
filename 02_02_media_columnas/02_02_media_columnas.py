import pandas as pd

df = pd.read_csv('empleados.csv', delimiter=";")
print(df.info())
print(df.mean(axis=0))