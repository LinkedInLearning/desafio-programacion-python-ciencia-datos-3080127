import pandas as pd

df = pd.read_csv('emisiones.csv', delimiter=";")
print(df.info())