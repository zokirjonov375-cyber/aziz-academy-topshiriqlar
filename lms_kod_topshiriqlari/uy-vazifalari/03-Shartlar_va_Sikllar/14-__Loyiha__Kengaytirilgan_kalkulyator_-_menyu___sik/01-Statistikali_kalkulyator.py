count = 0
total = 0
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
    else:
        valid = False
    if valid:
        print(result)
        count += 1
        total += result
print(f"Amallar: {count}")
print(f"Natijalar yig'indisi: {total}")
            
        