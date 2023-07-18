import pandas as pd
df = pd.read_csv('empleados.csv', delimiter=";")

print(df.head(20))
print(df.shape)
print(df.isnull().sum())
print(df.notnull().sum())
