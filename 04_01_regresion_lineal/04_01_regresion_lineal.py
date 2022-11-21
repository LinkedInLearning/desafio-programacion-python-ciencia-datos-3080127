import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('empleados.csv', delimiter=";")

print(df.head())

y = df['Salario'].values.reshape(-1,1)
X = df['Experiencia'].values.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

regresion_lineal = LinearRegression()

regresion_lineal.fit(X_train, y_train)

print('Coeficiente de regresión: ', regresion_lineal.coef_)
print('Puntaje de regresión: ',regresion_lineal.score(X_test, y_test))