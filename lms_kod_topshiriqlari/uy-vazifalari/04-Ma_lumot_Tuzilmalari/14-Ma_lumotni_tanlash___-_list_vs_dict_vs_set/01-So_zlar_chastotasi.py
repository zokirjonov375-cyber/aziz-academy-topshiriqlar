words = input().split()
counts = {}
for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1
for w in counts:
    print(w, counts[w])