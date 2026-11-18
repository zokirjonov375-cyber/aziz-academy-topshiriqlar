def jadval(son, nechtagacha=5):
    natijalar = []
    for i in range(1, nechtagacha + 1):
        natijalar.append(str(son * i))
    return " ".join(natijalar)
son = int(input())
nechtagacha = int(input())
print(jadval(son))
print(jadval(son, nechtagacha))