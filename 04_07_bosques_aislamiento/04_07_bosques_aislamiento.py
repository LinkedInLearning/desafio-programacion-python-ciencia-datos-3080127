import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv('empleados.csv', delimiter=";")

print(df.head())

isolation_forest = IsolationForest(random_state=42)
isolation_forest.fit(df[['Salario']])

df['Normal'] = isolation_forest.predict(df[['Salario']])

print(df[['Salario', 'Normal']])

print(df['Normal'].value_counts())