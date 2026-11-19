son = 0
def osir():
    global son
    son = son + 1
n = int(input())
for _ in range(n):
    osir()
print(son)