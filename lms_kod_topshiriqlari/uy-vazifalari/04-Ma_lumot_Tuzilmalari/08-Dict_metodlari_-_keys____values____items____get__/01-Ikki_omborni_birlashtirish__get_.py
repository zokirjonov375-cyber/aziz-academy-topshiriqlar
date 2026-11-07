n = int(input())
total = {}
for i in range(n):
    p = input().split()
    total[p[0]] = total.get(p[0], 0) + int(p[1])
m = int(input())
for i in range(m):
    p = input().split()
    total[p[0]] = total.get(p[0], 0) + int(p[1])
for name in sorted(total.keys()):
    print(name, total[name])