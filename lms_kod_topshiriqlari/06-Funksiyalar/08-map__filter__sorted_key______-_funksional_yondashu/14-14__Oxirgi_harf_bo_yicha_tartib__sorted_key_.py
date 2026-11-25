sozlar = input().split()
natija = sorted(sozlar, key=lambda s: s[-1])
print(' '.join(natija))