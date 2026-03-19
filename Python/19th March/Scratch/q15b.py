from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

data = load_iris()
X, y = data.data, data.target

model = DecisionTreeClassifier(criterion="gini")
model.fit(X, y)

print(model.predict(X[:5]))