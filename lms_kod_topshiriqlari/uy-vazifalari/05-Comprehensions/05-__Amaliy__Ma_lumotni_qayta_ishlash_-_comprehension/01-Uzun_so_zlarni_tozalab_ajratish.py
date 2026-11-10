words = input().split()
print([w.lower() for w in words if len(w) > 3])
