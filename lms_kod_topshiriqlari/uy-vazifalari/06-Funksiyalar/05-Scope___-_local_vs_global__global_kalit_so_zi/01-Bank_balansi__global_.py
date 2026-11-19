balans = 0
def kirim(x):
    global balans
    balans = balans + x
def chiqim(x):
    global balans
    balans = balans - x
n = int(input())
for _ in range(n):
    amal = input()
    belgi = amal[0]
    miqdor = int(amal[1:])
    if belgi == "+":
        kirim(miqdor)
    else:
        chiqim(miqdor)
print(balans)