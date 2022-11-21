from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score

X, y = make_regression()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)