prices = [int(x) for x in input().split()]
print([p + p * 12 // 100 for p in prices])
