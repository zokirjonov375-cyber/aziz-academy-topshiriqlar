parts = input().split()
target = int(input())
seen = set()
found = False
for p in parts:
    x = int(p)
    if(target - x) in seen:
        found = True
        break
    seen.add(x)
if found:
    print("Ha")
else:
    print("Yoq")