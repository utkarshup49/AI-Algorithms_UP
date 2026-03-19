def gini(data):
    total = len(data)
    count = {}
    for row in data:
        label = row[-1]
        count[label] = count.get(label,0) + 1

    g = 1
    for c in count.values():
        p = c/total
        g -= p*p
    return g

def gini_split(data, index):
    values = set([row[index] for row in data])
    weighted = 0

    for v in values:
        subset = [row for row in data if row[index] == v]
        weighted += (len(subset)/len(data)) * gini(subset)

    return weighted

print("Gini (Outlook):", gini_split(data, 0))
print("Gini (Temp):", gini_split(data, 1))