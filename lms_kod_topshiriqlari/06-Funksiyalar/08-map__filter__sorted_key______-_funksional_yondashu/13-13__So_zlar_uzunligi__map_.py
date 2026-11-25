sozlar = input().split()
uzunliklar = list(map(len, sozlar))
print(' '.join(map(str, uzunliklar)))