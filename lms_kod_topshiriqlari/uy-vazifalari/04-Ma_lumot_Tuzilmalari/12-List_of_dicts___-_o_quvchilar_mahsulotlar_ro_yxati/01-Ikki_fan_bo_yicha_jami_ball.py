n = int(input())
students = []
for i in range(n):
    parts = input().split()
    students.append({"ism": parts[0], "mat": int(parts[1]), "fiz": int(parts[2])})
for s in students:
    print(s["ism"], s["mat"] + s["fiz"])