import pandas as pd

df = pd.read_csv('temperaturas.csv', delimiter=";")
print(df.info())