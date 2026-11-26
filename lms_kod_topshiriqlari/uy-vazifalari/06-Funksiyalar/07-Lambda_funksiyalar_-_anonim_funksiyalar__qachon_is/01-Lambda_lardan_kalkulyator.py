amallar = { "+":lambda a, b: a + b, "-":lambda a, b: a - b, "*":lambda a, b: a * b,}
a, amal, b = input().split()
a = int(a)
b = int(b)
print(amallar[amal](a, b))