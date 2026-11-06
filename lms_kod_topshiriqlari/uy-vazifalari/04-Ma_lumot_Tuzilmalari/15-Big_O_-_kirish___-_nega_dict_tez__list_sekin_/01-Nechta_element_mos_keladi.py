a = set(input().split())
b = input().split()
count = 0
for x in b:
    if x in a:
        count += 1
print(count)