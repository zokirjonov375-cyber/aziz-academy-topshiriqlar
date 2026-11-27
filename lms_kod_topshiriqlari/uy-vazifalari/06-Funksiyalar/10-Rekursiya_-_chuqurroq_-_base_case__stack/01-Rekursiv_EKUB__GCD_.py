def ekub(a, b):
    if b == 0:
        return a
    return ekub(b, a % b)
a, b = input().split()
print(ekub(int(a), int(b)))