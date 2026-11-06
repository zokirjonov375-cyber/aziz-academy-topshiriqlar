n = int(input())
scores = {}
for i in range(n):
    parts = input().split()
    scores[parts[0]] = int(parts[1])
query = input()
print(scores[query])