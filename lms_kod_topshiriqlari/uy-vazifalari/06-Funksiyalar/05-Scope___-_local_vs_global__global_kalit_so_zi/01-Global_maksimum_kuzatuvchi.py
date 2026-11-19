eng_katta = 0
def tekshir(x):
    global eng_katta
    if x > eng_katta:
        eng_katta = x
sonlar = [int(x) for x in input().split()]
eng_katta = sonlar[0]
for s in sonlar:
    tekshir(s)
print(eng_katta)