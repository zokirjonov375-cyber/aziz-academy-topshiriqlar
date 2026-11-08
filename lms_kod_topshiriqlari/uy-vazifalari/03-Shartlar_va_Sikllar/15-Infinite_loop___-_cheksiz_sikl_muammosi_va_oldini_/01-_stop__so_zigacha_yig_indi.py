total = 0
while True:
    line = input()
    if line == "stop":
        break
    total += int(line)
print(total)