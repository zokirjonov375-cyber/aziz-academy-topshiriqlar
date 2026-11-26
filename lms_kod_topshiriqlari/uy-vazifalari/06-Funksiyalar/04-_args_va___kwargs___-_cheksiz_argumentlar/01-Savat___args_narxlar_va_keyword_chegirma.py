def savat(*narxlar, chegirma=0):
    jami = 0
    for n in narxlar:
        jami = jami + n
    return jami - jami * chegirma // 100
narxlar = [int(x) for x in input().split()]
chegirma = int(input())
print(savat(*narxlar, chegirma=chegirma))