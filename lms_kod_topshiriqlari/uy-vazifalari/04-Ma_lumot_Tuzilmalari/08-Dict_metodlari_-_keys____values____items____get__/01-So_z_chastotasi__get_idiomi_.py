words = input().split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
for w in sorted(freq.keys()):
    print(w, freq[w])