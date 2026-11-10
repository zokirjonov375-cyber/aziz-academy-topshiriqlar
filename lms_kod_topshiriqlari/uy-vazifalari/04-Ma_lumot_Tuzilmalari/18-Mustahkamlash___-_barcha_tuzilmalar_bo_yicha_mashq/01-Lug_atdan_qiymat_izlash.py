n = int(input())
d = {}
for i in range(n):
    parts = input().split()
    d[parts[0]] = parts[1]
q = input()
print(d.get(q, "Yo'q"))
    