juft = 0
toq = 0
def sanash(x):
    global juft, toq
    if x % 2 == 0:
        juft = juft + 1
    else:
        toq = toq + 1
sonlar = [int(x) for x in input().split()]
for s in sonlar:
    sanash(s)
print(juft, toq)