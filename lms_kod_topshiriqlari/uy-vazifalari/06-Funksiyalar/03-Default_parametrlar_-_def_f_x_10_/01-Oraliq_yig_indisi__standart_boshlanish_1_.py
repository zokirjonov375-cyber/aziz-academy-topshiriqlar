def yigindi(oxir, boshlanish=1):
    s = 0
    for i in range(boshlanish, oxir + 1):
        s = s + i
    return s
oxir = int(input())
boshlanish = int(input())
print(yigindi(oxir))
print(yigindi(oxir, boshlanish))
