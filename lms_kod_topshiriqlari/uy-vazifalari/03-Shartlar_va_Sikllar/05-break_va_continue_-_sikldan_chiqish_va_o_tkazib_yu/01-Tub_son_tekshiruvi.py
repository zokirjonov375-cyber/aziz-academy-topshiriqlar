n = int(input())
is_prime = 1
if n < 2:
    is_prime = 0
d = 2
while d * d <= n:
    if n % d == 0:
        is_prime = 0
        break
    d = d + 1
if is_prime == 1:
    print("ha")
else:
    print("yo'q")