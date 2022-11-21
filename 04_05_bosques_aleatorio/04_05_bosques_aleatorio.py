from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

X, y = make_classification(n_samples=5000,  n_features=20, random_state=3)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)