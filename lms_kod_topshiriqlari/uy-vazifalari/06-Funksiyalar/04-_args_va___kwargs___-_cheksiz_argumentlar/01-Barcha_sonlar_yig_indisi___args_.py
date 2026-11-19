def yigindi(*sonlar):
    s = 0
    for x in sonlar:
        s = s + x
    return s
sonlar = [int(x) for x in input().split()]
print(yigindi(*sonlar))