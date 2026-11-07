n = int(input())
students = []
for i in range(n):
    parts = input().split()
    students.append({"name": parts[0], "score": int(parts[1])})
w = len("O'rtacha")
for s in students:
    if len(s["name"]) > w:
        w = len(s["name"])
total = 0
for s in students:
    total += s["score"]
    print(s["name"].ljust(w) + str(s["score"]).rjust(5))
avg = total // n
print("O'rtacha".ljust(w) + str(avg).rjust(5))