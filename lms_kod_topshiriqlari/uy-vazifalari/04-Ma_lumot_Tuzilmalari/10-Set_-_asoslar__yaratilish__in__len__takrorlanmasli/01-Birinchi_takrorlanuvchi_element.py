nums = input().split()
seen = set()
answer = None
for x in nums:
    if x in seen:
        answer = x
        break
    seen.add(x)
if answer is None:
    print("Yo'q")
else:
    print(answer)