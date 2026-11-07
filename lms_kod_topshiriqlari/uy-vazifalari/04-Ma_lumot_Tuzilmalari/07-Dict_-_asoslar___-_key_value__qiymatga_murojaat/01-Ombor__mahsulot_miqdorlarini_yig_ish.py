n = int(input())
totals = {}
order = []
for i in range(n):
    parts = input().split()
    name = parts[0]
    amount = int(parts[1])
    if name in totals:
        totals[name] += amount
    else:
        totals[name] = amount
        order.append(name)
for name in order:
    print(name, totals[name])