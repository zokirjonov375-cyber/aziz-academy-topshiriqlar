def baho(a, b, c):
    ortacha = (a + b + c) / 3
    if ortacha >= 90:
        return "a'lo"
    elif ortacha >= 70:
        return "yaxshi"
    elif ortacha >= 60:
        return "qoniqarli"
    else:
        return "qoniqarsiz"
a = int(input())
b = int(input())
c = int(input())
print(baho(a, b, c))