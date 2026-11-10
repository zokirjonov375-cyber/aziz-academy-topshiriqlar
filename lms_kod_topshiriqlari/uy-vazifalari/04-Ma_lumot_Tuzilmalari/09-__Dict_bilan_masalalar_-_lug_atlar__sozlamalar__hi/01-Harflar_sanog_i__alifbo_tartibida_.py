s = input()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
for ch in sorted(freq):
    print(ch, freq[ch])