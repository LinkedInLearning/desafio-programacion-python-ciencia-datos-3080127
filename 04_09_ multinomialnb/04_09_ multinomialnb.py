from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

df = pd.read_csv('solicitudes.csv', delimiter=";")

X = df['Asunto']
y = df['Categoría']

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)

count_vectorizer = CountVectorizer()
X_train_dtm = count_vectorizer.fit_transform(X_train)

X_test_dtm = count_vectorizer.transform(X_test)

multinomia_nb = MultinomialNB()
multinomia_nb.fit(X_train_dtm, y_train)

y_pred_class = multinomia_nb.predict(X_test_dtm)

print('La presición es: ', accuracy_score(y_test, y_pred_class))
print('F1 Score: ', f1_score(y_test, y_pred_class, average="macro"))