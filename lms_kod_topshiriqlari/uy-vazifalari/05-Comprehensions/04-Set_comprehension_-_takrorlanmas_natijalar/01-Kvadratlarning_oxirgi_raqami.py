nums = [int(x) for x in input().split()]
res = list({(x * x) % 10 for x in nums})
res.sort()
print(res)