import pandas as pd
import seaborn as sns

df = pd.read_csv('empleados.csv', delimiter=";")
print(df.head(20))