import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

n = len(X)

sum_x = sum(X)
sum_y = sum(Y)
sum_xy = sum([X[i]*Y[i] for i in range(n)])
sum_x2 = sum([x*x for x in X])

m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x*sum_x)
c = (sum_y - m*sum_x) / n

Y_pred = [m*x + c for x in X]

plt.scatter(X, Y)
plt.plot(X, Y_pred)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression")
plt.show()
