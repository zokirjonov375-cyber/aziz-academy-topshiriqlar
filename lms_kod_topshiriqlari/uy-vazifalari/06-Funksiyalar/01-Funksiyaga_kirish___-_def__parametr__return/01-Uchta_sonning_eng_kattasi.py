def eng_katta(a, b, c):
    m = a
    if b > m:
        m = b
    if c > m:
            m = c
    return m
a = int(input())
b = int(input())
c = int(input())
print(eng_katta(a, b, c))
