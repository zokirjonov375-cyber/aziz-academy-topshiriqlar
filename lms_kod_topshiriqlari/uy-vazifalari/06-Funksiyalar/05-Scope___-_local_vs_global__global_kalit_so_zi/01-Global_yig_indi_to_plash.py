jami = 0
def qosh(x):
    global jami
    jami = jami + x
sonlar = [int(x) for x in input().split()]
for s in sonlar:
    qosh(s)
print(jami)