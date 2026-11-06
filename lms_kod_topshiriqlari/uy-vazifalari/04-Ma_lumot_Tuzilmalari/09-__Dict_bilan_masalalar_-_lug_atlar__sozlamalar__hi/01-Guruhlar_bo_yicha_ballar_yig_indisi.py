n = int(input())
totals = {}
for i in range(n):
    p = input().split()
    totals[p[0]] = totals.get(p[0], 0) + int(p[1])
for g in sorted(totals):
    print(g, totals[g])