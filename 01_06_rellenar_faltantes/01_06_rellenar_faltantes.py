import pandas as pd
df = pd.read_csv('empleados.csv', delimiter=";")

print(df)
print(df.isnull().sum())