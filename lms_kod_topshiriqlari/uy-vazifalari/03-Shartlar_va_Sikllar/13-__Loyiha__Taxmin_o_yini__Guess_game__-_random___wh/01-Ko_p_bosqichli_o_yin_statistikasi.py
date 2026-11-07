r = int(input())
total = 0
best = None
for round_no in range(1, r+1):
    secret = int(input())
    attempts = 0
    while True:
        guess = int(input())
        attempts += 1
        if guess == secret:
            break
    total += attempts
    if best is None or attempts < best:
        best = attempts
    print(f"Round {round_no}: {attempts} urinish")
print(f"Jami: {total}")
print(f"Eng yaxshi: {best}")