import pandas as pd
df = pd.read_csv('empleados.csv', delimiter=";")

print(df.head(20))
print(df.shape)
print(df[df.isnull().any(axis=1)])
df_actualizado = df.dropna(axis=0)
print(df_actualizado)
df_actualizado = df.dropna(axis=0, thresh=5)
print(df_actualizado)