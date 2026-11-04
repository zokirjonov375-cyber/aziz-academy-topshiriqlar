items = input().split()
seen = set()
ans = "yoq"
for x in items:
    if x in seen:
        ans = x
        break
    seen.add(x)
print(ans)