a = set(input().split())
b = set(input().split())
count = 0
for x in a:
    if x in b:
        count += 1
print(count)