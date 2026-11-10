words = input().split()
seen = {}
for w in words:
    seen[w] = True
print(len(seen))