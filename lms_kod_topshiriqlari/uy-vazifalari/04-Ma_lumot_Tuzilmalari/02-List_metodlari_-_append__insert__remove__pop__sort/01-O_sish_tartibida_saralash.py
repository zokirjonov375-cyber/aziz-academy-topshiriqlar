n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()
res = ""
for x in lst:
    if res == "":
        res = str(x)
    else:
        res = res + " " + str(x)
print(res)
