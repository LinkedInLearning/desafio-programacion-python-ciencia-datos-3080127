import pandas as pd
df = pd.read_csv('empleados.csv', delimiter=";")

print(df.shape)

duplicados = df.duplicated()
print(df[duplicados])