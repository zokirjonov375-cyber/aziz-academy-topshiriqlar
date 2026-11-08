result = 0
while True:
    op = input()
    if op == "=":
        break
    x = int(input())
    if op == "+":
        result += x
    elif op == "-":
        result -= x
    elif op == "*":
        result *= x
    elif op == "/":
        if x != 0:
            result //= x
print(result)
        
    