sonlar = [int(x) for x in input().split()]
juftlar = filter(lambda x: x % 2 == 0, sonlar)
kvadratlar = map(lambda x: x * x, juftlar)
natija = sorted(kvadratlar, reverse=True)
print(*natija)