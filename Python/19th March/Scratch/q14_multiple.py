X1 = [1,2,3,4,5]
X2 = [2,1,3,5,4]
Y  = [3,3,6,9,9]

n = len(X1)

sum_x1 = sum(X1)
sum_x2 = sum(X2)
sum_y  = sum(Y)

sum_x1x1 = sum([x*x for x in X1])
sum_x2x2 = sum([x*x for x in X2])
sum_x1x2 = sum([X1[i]*X2[i] for i in range(n)])

sum_x1y = sum([X1[i]*Y[i] for i in range(n)])
sum_x2y = sum([X2[i]*Y[i] for i in range(n)])

A = [
    [n, sum_x1, sum_x2],
    [sum_x1, sum_x1x1, sum_x1x2],
    [sum_x2, sum_x1x2, sum_x2x2]
]

B = [sum_y, sum_x1y, sum_x2y]

def solve(A, B):
    for i in range(3):
        pivot = A[i][i]
        for j in range(3):
            A[i][j] /= pivot
        B[i] /= pivot

        for k in range(3):
            if k != i:
                factor = A[k][i]
                for j in range(3):
                    A[k][j] -= factor * A[i][j]
                B[k] -= factor * B[i]
    return B

b0, b1, b2 = solve(A, B)

print("Intercept:", b0)
print("b1:", b1)
print("b2:", b2)