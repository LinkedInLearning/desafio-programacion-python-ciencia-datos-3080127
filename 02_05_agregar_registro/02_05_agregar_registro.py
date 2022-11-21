import pandas as pd

df = pd.read_csv('temperaturas.csv', delimiter=";")
print(df)

nueva_temperatura = pd.DataFrame.from_dict([{'Año': '2022', 'Temperatura': '74.3'}])