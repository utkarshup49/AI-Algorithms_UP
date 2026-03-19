import math

X = [1,2,3,4,5]
Y = [0,0,0,1,1]

w = 0
b = 0
lr = 0.1

def sigmoid(z):
    return 1/(1 + math.exp(-z))

for epoch in range(1000):
    dw = 0
    db = 0

    for i in range(len(X)):
        z = w*X[i] + b
        y_pred = sigmoid(z)

        dw += (y_pred - Y[i]) * X[i]
        db += (y_pred - Y[i])

    w -= lr * dw
    b -= lr * db

print("Weight:", w)
print("Bias:", b)

for x in X:
    print(sigmoid(w*x + b))
