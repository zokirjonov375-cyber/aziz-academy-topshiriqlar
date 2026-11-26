sonlar = [int(x) for x in input().split()]
musbatlar = filter(lambda x: x > 0, sonlar)
natija = list(map(lambda x: x * 2, musbatlar))
print(*natija)