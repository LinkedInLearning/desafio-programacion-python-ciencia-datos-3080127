import pandas as pd
df = pd.read_csv('empleados.csv', delimiter=";")

print(df.head(20))
print(df.shape)
print(df.isnull().sum())

df_actualizado = df.drop(axis=1, columns=['Apellido'])
print(df_actualizado.head(20))