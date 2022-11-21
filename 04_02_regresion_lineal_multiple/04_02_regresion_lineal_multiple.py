import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np

df = pd.read_csv('emisiones.csv', delimiter=";")

print(df.info())

y = df[['CO2']]
X = df[['Longitud', 'Anchura', 'Altura']]