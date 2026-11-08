n = int(input())
students = []
for i in range(n):
    parts = input().split()
    students.append({"ism": parts[0], "yosh": int(parts[1])})
best = students[0]
for s in students:
    if s["yosh"] > best["yosh"]:
        best = s
print(best["ism"])