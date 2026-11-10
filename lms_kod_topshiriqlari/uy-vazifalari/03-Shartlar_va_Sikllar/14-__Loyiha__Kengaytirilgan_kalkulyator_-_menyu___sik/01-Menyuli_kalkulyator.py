while True:
    choice = input()
    if choice == "0":
        break
    a = int(input())
    b = int(input())
    if choice == "1":
        print(a + b)
    elif choice == "2":
        print(a - b)
    elif choice == "3":
        print(a * b)
    elif choice == "4":
        if b == 0:
            print("Xato")
        else:
            print(a // b)
    else:
        print("Noma'lum")
            