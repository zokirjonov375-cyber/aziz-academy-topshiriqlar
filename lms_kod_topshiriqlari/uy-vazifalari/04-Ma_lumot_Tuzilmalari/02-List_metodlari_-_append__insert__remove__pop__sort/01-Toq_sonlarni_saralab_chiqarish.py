n = int(input())
odds = []
for i in range(n):
    x = int(input())
    if x % 2 != 0:
        odds.append(x)
odds.sort()
res = ""
for v in odds:
    if res == "":
        res = str(v)
    else:
        res = res + " " + str(v)
print(res)