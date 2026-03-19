import math

data = [
    ['Sunny','Hot','No'],
    ['Sunny','Hot','No'],
    ['Overcast','Hot','Yes'],
    ['Rain','Mild','Yes'],
    ['Rain','Cool','Yes']
]

def entropy(data):
    total = len(data)
    count = {}
    for row in data:
        label = row[-1]
        count[label] = count.get(label,0) + 1

    ent = 0
    for c in count.values():
        p = c/total
        ent -= p * math.log2(p)
    return ent

def split(data, index, value):
    return [row for row in data if row[index] == value]

def info_gain(data, index):
    total_entropy = entropy(data)
    values = set([row[index] for row in data])

    weighted = 0
    for v in values:
        subset = split(data, index, v)
        weighted += (len(subset)/len(data)) * entropy(subset)

    return total_entropy - weighted

print("Entropy:", entropy(data))
print("Gain (Outlook):", info_gain(data, 0))
print("Gain (Temp):", info_gain(data, 1))
