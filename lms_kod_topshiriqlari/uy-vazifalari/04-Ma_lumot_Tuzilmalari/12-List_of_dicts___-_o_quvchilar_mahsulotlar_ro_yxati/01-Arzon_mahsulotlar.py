n = int(input())
products = []
for i in range(n):
    parts = input().split()
    products.append({"nom": parts[0], "narx": int(parts[1])})
limit = int(input())
for p in products:
    if p["narx"] < limit:
        print(p["nom"])
    