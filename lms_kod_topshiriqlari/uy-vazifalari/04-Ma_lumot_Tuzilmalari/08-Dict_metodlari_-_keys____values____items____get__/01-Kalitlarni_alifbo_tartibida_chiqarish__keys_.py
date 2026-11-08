n = int(input())
d = {}
for i in range(n):
    p = input().split()
    d[p[0]] = int(p[1])
print(" ".join(sorted(d.keys())))