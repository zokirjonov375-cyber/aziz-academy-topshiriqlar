def royxat_yigindisi(sonlar):
    if len(sonlar) == 0:
        return 0
    return sonlar[0] + royxat_yigindisi(sonlar[1:])
sonlar = [int(x) for x in input().split()]
print(royxat_yigindisi(sonlar))