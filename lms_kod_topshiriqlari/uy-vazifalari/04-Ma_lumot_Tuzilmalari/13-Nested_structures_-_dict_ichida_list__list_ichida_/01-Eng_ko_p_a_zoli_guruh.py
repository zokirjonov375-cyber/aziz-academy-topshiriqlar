n = int(input())
groups = {}
for i in range(n):
    parts = input().split()
    groups[parts[0]] = parts[1:]
best = None
best_count = -1
for g in groups:
    if len(groups[g]) > best_count:
        best_count = len(groups[g])
        best = g
print(best)
        
    