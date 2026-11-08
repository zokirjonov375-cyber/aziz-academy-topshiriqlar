n = int(input())
d = {}
for i in range(n):
    p = input().split()
    d[p[0]] = int(p[1])
best_name = None
best_score = None
for name, score in sorted(d.items()):
    if best_score is None or score > best_score:
        best_name = name
        best_score = score
print(best_name, best_score)
