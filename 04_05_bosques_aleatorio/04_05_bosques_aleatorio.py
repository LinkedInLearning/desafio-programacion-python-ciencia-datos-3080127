from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

X, y = make_classification(n_samples=5000,  n_features=20, random_state=3)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

bosques_aleatorio = RandomForestClassifier(random_state=42)
bosques_aleatorio.fit(X_train, y_train)

precision = bosques_aleatorio.score(X_test, y_test)
print('La precisión es ', precision*100)

y_pred = bosques_aleatorio.predict(X_test)
matriz_confusion = confusion_matrix(y_test,y_pred)

plt.subplots(figsize = (4,4))
sns.heatmap(matriz_confusion, annot = True, fmt =".0f")
plt.xlabel("Predicción")
plt.ylabel("Actual")
plt.show()