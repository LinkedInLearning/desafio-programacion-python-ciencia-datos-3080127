import pandas as pd
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('datos.csv', delimiter=";")
print(df.head(20))

scaler = MinMaxScaler()