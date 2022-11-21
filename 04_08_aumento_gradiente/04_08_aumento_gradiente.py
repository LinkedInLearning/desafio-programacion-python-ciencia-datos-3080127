from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score

X, y = make_regression()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

gradient_boosting_regressor = GradientBoostingRegressor()
gradient_boosting_regressor.fit(X_train, y_train)

pred_y=gradient_boosting_regressor.predict(X_test)
print("Coeficiente de determinación o R2: ", r2_score(y_test,pred_y)*100)