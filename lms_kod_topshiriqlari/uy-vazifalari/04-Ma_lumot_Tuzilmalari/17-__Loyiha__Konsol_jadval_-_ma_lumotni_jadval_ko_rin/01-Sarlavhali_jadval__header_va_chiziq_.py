n = int(input())
print("Mahsulot".ljust(10) + "Soni".rjust(6))
print("-" * 16)
for i in range(n):
    parts = input().split()
    print(parts[0].ljust(10) + parts[1].rjust(6))