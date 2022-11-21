import pandas as pd
df = pd.read_csv('empleados.csv', delimiter=";")

print(df)
print(df.isnull().sum())

df['Edad']=df['Edad'].fillna(df['Edad'].mean())
print(df.isnull().sum())