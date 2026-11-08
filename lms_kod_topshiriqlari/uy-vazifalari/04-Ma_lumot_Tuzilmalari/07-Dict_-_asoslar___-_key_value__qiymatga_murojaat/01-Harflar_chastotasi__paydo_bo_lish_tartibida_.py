s = input()
counts = {}
order = []
for ch in s:
    if ch in counts:
        counts[ch] += 1
    else:
        counts[ch] = 1
        order.append(ch)
for ch in order:
    print(ch, counts[ch])