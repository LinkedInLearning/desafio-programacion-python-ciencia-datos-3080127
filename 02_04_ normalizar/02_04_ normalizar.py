import pandas as pd
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('datos.csv', delimiter=";")
print(df.head(20))

scaler = MinMaxScaler()

scaled_df = scaler.fit_transform(df)

scaled_df = pd.DataFrame(scaled_df, columns=['Altura', 'Peso'])

print (scaled_df)