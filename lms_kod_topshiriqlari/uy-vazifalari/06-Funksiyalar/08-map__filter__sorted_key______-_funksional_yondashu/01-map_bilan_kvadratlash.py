sonlar = [int(x) for x in input().split()]
natija = list(map(lambda x: x * x, sonlar))
print(*natija)