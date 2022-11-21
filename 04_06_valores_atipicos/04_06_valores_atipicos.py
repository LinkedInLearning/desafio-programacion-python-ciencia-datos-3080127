import pandas as pd
from sklearn.neighbors import LocalOutlierFactor

df = pd.read_csv('datos.csv', delimiter=";")

local_outlier_factor = LocalOutlierFactor()
local_outlier_factor.fit(df)

df['local_outlier'] = local_outlier_factor.fit_predict(df)

print(df['local_outlier'].value_counts())