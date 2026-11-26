def yigindi(n):
    if n == 0:
        return 0
    return n + yigindi(n - 1)
n = int(input())
print(yigindi(n))