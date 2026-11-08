nums = input().split()
t = int(input())
res = ""
for x in nums:
    if int(x) > t:
        if res == "":
            res = x
        else:
            res = res + " " + x 
print(res)