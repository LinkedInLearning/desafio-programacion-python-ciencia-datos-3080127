import pandas as pd

df = pd.read_csv('emisiones.csv', delimiter=";")
print(df.info())

columnas_numericas = df.select_dtypes(include=['float', 'int'])
print(columnas_numericas)