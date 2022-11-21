import pandas as pd

df = pd.read_csv('temperaturas.csv', delimiter=";")
print(df.info())

print(df['temperatura'].min())
print(df['temperatura'].max())
print(df['temperatura'].mean())
print(df['temperatura'].std())
print(df["temperatura"].var())