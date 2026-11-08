n = int(input())
a, b = 0,1
res = []
for i in range(n):
    res.append(str(a))
    a, b = b, a + b
print(" ".join(res))