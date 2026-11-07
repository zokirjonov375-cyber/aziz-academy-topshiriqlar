nums = input().split()
res = ""
for i in range(len(nums) - 1, -1, -1):
    if res == "":
        res = nums[i]
    else:
        res = res + " " + nums[i]
print(res)