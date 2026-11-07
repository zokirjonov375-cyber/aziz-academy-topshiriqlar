n = int(input())
book = {}
for i in range(n):
    parts = input().split()
    book[parts[0]] = parts[1]
q = int(input())
for i in range(q):
    name = input()
    if name in book:
        print(book[name])
    else:
        print("topilmadi")
