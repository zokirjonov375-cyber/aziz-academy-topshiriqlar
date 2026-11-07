n = int(input())
votes = {}
order = []
for i in range(n):
    name = input()
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1
        order.append(name)
best = order[0]
for name in order:
    if votes[name] > votes[best]:
        best = name
print(best)
        