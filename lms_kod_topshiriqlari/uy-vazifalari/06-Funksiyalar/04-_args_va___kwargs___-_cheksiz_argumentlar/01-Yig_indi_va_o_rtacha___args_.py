def hisobot(*sonlar):
    s = 0
    for x in sonlar:
        s = s + x
    return f"{s} {s // len(sonlar)}"
sonlar = [int(x) for x in input().split()]
print(hisobot(*sonlar))
