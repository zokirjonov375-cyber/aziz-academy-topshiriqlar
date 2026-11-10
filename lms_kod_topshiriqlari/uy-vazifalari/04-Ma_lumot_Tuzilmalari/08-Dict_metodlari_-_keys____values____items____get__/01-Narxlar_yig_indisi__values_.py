n = int(input())
prices = {}
for i in range(n):
    p = input().split()
    prices[p[0]] = int(p[1])
print(sum(prices.values()))