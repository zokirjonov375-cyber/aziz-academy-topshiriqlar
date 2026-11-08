n = int(input())
for i in range(n):
    parts = input().split()
    name = parts[0]
    price = parts[1]
    print(name.ljust(10) + price.rjust(6))