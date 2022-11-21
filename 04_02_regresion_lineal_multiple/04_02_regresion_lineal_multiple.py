import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np

df = pd.read_csv('emisiones.csv', delimiter=";")

print(df.info())

y = df[['CO2']]
X = df[['Longitud', 'Anchura', 'Altura']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

regresion_lineal = LinearRegression()

regresion_lineal.fit(X_train, y_train)
y_pred=regresion_lineal.predict(X_test)

print("Error absoluto medio: ", metrics.mean_absolute_error(y_test, y_pred))
print("Error cuadrático medio: ", metrics.mean_squared_error(y_test, y_pred))
print("Raíz del error cuadrático medio: ",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))