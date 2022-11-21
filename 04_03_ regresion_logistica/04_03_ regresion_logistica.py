import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

df = pd.read_csv('examenes.csv', delimiter=";")

X = df['Horas'].values.reshape(-1,1)
y = df['Puntaje']