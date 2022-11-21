import pandas as pd
import seaborn as sns

df = pd.read_csv('empleados.csv', delimiter=";")
print(df.head(20))

df['Experiencia'].corr(df['Salario'])
sns.heatmap(df.corr(numeric_only=True), vmin=-1, vmax=1, annot=True)