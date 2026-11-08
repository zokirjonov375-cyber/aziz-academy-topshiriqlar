nums = [int(x) for x in input().split()]
print([x * x for x in nums if x % 3 == 0])