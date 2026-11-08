n = int(input())
groups = {}
for i in range(n):
    parts = input().split()
    groups[parts[0]] = parts[1:]
q = input().split()
gname = q[0]
person = q[1]
if person in groups[gname]:
    print("Ha")
else:
    print("Yoq")