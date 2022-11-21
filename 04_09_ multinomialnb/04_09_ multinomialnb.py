from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

df = pd.read_csv('solicitudes.csv', delimiter=";")

X = df['Asunto']
y = df['Categoría']


