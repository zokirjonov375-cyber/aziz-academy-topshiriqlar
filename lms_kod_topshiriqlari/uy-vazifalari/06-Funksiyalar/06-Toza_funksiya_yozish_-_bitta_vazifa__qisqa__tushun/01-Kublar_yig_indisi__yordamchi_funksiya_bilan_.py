def kub(x):
    return x * x * x
def yigindi_kublari(n):
    s = 0
    for i in range(1, n + 1):
        s = s + kub(i)
    return s
n = int(input())
print(yigindi_kublari(n))