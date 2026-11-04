n = int(input())
rows = []
for i in range(n):
    parts = input().split()
    name = parts[0]
    score = int(parts[1])
    rows.append((-score, name))
rows.sort()
for neg_score, name in rows:
    print(name, -neg_score)