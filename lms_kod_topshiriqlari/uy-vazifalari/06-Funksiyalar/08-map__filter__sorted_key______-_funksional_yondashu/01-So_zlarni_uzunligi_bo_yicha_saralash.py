sozlar = input().split()
natija = sorted(sozlar, key=lambda s: len(s))
print(*natija)