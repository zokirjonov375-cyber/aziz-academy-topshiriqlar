n = int(input())
talabalar = []
for _ in range(n):
    ism, ball = input().split()
    talabalar.append((ism, int(ball)))
talabalar = sorted(talabalar, key= lambda t: t[1], reverse=True)
for ism, ball in talabalar:
    print(ism, ball)