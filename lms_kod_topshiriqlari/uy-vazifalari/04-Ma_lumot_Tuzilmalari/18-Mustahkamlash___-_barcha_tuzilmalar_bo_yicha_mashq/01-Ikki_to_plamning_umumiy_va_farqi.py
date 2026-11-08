a = set()
for x in input().split():
    a.add(int(x))
b = set()
for x in input().split():
    b.add(int(x))
common = sorted(a & b)
onlya = sorted(a - b)
part1 = []
for x in common:
    part1.append(str(x))
part2 = []
for x in onlya:
    part2.append(str(x))
print(" ".join(part1))
print(" ".join(part2))