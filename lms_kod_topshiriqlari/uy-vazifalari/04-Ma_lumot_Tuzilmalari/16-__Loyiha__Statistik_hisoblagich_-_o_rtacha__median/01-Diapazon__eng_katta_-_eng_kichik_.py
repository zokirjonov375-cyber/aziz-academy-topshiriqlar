nums = []
for x in input().split():
    nums.append(int(x))
mx = nums[0]
mn = nums[0]
for x in nums:
    if x > mx:
        mx = x
    if x < mn:
        mn = x
print(mx - mn)
        
        