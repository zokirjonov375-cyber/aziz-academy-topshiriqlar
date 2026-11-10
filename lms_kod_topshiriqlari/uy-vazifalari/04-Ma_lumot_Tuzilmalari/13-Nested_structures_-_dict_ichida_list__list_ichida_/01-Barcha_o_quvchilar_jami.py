n = int(input())
total = 0
for i in range(n):
    parts = input().split()
    members = parts[1:]
    total += len(members)
print(total)