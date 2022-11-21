import pandas as pd
from sklearn.linear_model import LinearRegression

regresion_lineal = LinearRegression()
df = pd.read_csv('empleados.csv', delimiter=";")

print(df.head(20))
print(df.isnull().sum())

datos_test = df[df['Edad'].isnull()==True]
datos_entrenamiento = df[df['Edad'].isnull()==False]

y_entrenamiento = datos_entrenamiento['Edad']
x_entranamiento = datos_entrenamiento.drop("Edad",axis=1)

regresion_lineal.fit(x_entranamiento,y_entrenamiento)

datos_test = datos_test.drop("Edad",axis=1)

predicciones = regresion_lineal.predict(datos_test)
print(predicciones)

datos_test['Edad']= predicciones

print(datos_test)