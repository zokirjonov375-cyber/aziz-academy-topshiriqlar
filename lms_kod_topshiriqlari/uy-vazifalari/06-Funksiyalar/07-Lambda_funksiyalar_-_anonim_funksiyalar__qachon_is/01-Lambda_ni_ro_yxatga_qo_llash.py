f = lambda x: x * x + 1
sonlar = [int(x) for x in input().split()]
natija = [f(x) for x in sonlar]
print(*natija)