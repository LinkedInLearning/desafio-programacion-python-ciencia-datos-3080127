import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

df = pd.read_csv('examenes.csv', delimiter=";")

X = df['Horas'].values.reshape(-1,1)
y = df['Puntaje']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

logistic_regression = LogisticRegression(max_iter=1000)
logistic_regression.fit(X_train, y_train)

horas_test = np.array([5, 6, 7, 8, 9, 10]).reshape(-1,1)
y_pred = logistic_regression.predict(horas_test)

print(y_pred)