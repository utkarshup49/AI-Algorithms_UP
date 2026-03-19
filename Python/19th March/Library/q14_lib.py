import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = np.loadtxt("Advertising.csv", delimiter=",", skiprows=1)

X = data[:, 1:4]
y = data[:, 4]

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

plt.scatter(X[:, 0], y)
plt.plot(X[:, 0], y_pred)
plt.show()

print(model.coef_, model.intercept_)
