nums = input().split()
res = ""
for x in nums:
    d = int(x) * 2
    if res == "":
        res = str(d)
    else:
        res = res + " " + str(d)
print(res)