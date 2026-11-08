n = int(input())
students = []
for i in range(n):
    parts = input().split()
    students.append({"ism": parts[0], "baholar": parts[1:]})
for s in students:
    total = 0
    for b in s["baholar"]:
        total += int(b)
    print(s["ism"], total)