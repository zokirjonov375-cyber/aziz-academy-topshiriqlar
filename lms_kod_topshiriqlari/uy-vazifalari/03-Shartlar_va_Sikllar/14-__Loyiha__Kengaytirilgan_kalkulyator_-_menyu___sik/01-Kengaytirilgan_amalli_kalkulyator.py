best = None
while True:
    choice = input()
    if choice == "0":
        break
    a = int(input())
    b = int(input())
    result = 0
    valid = True
    if choice == "1":
        result = a + b
    elif choice == "2":
        result = a - b
    elif choice == "3":
        result = a * b
    elif choice == "4":
        if b == 0:
            valid = False
        else:
            result = a // b
    elif choice == "5":
        result = a ** b
    elif choice == "6":
        if b == 0:
            valid = False
        else:
            result = a % b
    else:
        valid = False
    if valid:
        print(result)
        if best is None or result > best:
            best = result
print(f"Eng katta natija: {best}")
        