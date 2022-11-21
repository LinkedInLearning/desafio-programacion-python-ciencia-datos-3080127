import pandas as pd
from sklearn.linear_model import LinearRegression

regresion_lineal = LinearRegression()

df = pd.read_csv('empleados.csv', delimiter=";")

print(df.head(20))
print(df.isnull().sum())