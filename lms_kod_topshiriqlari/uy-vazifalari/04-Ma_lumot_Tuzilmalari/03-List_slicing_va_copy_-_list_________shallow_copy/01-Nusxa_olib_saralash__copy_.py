nums = []
for x in input().split():
     nums.append(int(x))
copy = nums[:]
copy.sort()
res1 = ""
for v in nums:
    if res1 == "":
        res1 = str(v)
    else:
        res1 = res1 + " " + str(v)
res2 = ""
for v in copy:
    if res2 == "":
        res2 = str(v)
    else:
        res2 = res2 + " " + str(v)
print(res1)
print(res2)
        
