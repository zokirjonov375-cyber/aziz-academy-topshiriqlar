n = int(input())
stock = {}
for i in range(n):
    parts = input().split()
    item = parts[0]
    qty = int(parts[1])
    if item in stock:
        stock[item] += qty
    else:
        stock[item] = qty
m = int(input())
for i in range(m):
    parts = input().split()
    item = parts[0]
    qty = int(parts[1])
    if item in stock:
        stock[item] += qty
    else:
        stock[item] = qty
for item in sorted(stock):
    print(item, stock[item])
    