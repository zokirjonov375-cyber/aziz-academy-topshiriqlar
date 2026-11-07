n = int(input())
names = []
score = {}
for i in range(n):
    p = input().split()
    names.append(p[0])
    score[p[0]] = int(p[1])
remaining = list(names)
result = []
while remaining:
    best = None
    for name in sorted(remaining):
        if best is None or score[name] > score[best]:
            best = name
    result.append(best)
    remaining.remove(best)
for name in result:
    print(name, score[name])
            