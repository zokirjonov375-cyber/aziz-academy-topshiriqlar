prices = [int(x) for x in input().split()]
print({p: p - p // 10 for p in prices if p >= 100})