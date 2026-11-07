first = input().split()
second = input().split()
in_first = {}
for w in first:
    in_first[w] = True
common = {}
for w in second:
    if w in in_first:
        common[w] = True
for w in sorted(common):
    print(w)