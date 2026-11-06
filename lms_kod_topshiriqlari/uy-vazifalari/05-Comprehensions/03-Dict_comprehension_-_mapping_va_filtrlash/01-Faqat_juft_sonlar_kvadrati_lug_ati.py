nums = [int(x) for x in input().split()]
print({x:x * x for x in nums if x % 2 == 0})