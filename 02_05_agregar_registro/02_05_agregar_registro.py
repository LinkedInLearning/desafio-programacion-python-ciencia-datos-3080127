import pandas as pd

df = pd.read_csv('temperaturas.csv', delimiter=";")
print(df)

nueva_temperatura = pd.DataFrame.from_dict([{'Año': '2022', 'Temperatura': '74.3'}])

df = pd.concat([df, nueva_temperatura], ignore_index=True)

print(df)