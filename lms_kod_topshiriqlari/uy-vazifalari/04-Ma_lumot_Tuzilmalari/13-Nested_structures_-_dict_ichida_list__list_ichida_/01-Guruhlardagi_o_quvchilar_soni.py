n = int(input())
groups = {}
for i in range(n):
    parts = input().split()
    groups[parts[0]] = parts[1:]
for g in groups:
    print(g, len(groups[g]))
    