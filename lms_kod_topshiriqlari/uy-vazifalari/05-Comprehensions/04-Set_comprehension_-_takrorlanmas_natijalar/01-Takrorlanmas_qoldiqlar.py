nums = [int(x) for x in input().split()]
res = list({x % 3 for x in nums})
res.sort()
print(res)