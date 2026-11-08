s = 0
while True:
    x = int(input())
    if x == 0:
        break
    if x < 0:
        continue
    if x > 100:
        break
    s = s + x
print(s)        
    