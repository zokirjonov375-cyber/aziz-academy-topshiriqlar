def raqam_yigindisi(n):
    if n < 10:
        return n
    return n % 10 + raqam_yigindisi(n // 10)
n = int(input())
print(raqam_yigindisi(n))