import math

data = [
    [5.1,3.5,1.4,0.2,'A'],
    [4.9,3.0,1.4,0.2,'A'],
    [6.2,3.4,5.4,2.3,'B'],
    [5.9,3.0,5.1,1.8,'B']
]

def distance(a, b):
    return math.sqrt(sum((a[i]-b[i])**2 for i in range(len(a))))

def knn(train, test, k):
    distances = []

    for row in train:
        d = distance(test, row[:-1])
        distances.append((d, row[-1]))

    distances.sort()

    neighbors = distances[:k]
    votes = {}

    for _, label in neighbors:
        votes[label] = votes.get(label,0) + 1

    return max(votes, key=votes.get)

test = [5.0,3.4,1.5,0.2]

prediction = knn(data, test, 3)
print("Prediction:", prediction)
