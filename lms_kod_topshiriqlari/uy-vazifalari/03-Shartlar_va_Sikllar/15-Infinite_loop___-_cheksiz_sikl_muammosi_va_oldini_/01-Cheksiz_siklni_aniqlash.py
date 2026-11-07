start = int(input())
step = int(input())
if step <= 0:
    print("CHEKSIZ")
else:
    value = start
    count = 0
    while value < 100:
        value += step
        count += 1
    print(count)
    