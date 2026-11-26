def daraja(a, b):
    if b == 0:
        return 1
    return a * daraja(a, b - 1)
a, b = input().split()
print(daraja(int(a), int(b)))