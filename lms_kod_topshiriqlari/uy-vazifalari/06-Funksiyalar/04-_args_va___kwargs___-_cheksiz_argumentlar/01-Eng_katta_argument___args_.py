def eng_katta(*sonlar):
    m = sonlar[0]
    for x in sonlar:
        if x > m:
            m = x
    return m
sonlar = [int(x) for x in input().split()]
print(eng_katta(*sonlar))
        