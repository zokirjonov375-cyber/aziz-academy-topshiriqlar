sonlar = [int(x) for x in input().split()]
natija = list(filter(lambda x: x % 2 == 0, sonlar))
print(*natija)