import pandas as pd

df = pd.read_csv('emisiones.csv', delimiter=";")
print(df.head(10))

df = df.iloc[:,[0,1,3,2,4]]

print(df)