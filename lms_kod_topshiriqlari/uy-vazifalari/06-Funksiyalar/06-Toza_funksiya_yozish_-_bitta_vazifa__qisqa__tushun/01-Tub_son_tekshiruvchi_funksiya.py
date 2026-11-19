def tub_mi(n):
    if n < 2:
        return False
    d = 2
    while d < n:
        if n % d == 0:
            return False
        d = d + 1
    return True
son = int(input())
if tub_mi(son):
    print("Ha")
else:
    print("Yo'q")
    