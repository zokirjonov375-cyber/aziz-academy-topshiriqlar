nums = input().split()
res = ""
for x in nums:
    if int(x) % 2 == 0:
        if res == "":
            res = x
        else:
            res = res + " " + x
print(res)