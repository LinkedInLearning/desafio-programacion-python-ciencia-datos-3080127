import pandas as pd
from sklearn.neighbors import LocalOutlierFactor

df = pd.read_csv('datos.csv', delimiter=";")