n = int(input())
students = []
for i in range(n):
    parts = input().split()
    students.append({"ism": parts[0], "yosh": int(parts[1])})
for s in students:
        print(s["ism"])