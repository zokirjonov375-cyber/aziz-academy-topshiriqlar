n = int(input())
students = []
for i in range(n):
    parts = input().split()
    students.append({"ism": parts[0], "baholar": parts[1:]})
best_ism = None
best_val = -1
for s in students:
    for b in s["baholar"]:
        v = int(b)
        if v > best_val:
            best_val = v
            best_ism = s["ism"]
print(best_ism, best_val)
