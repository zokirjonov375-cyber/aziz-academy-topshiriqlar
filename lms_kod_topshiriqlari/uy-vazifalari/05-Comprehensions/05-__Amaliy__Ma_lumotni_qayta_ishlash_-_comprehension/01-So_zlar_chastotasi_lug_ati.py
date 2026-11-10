words = input().split()
print({w: words.count(w) for w in words})