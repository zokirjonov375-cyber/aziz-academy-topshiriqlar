def perimetr(eni, boyi):
    return 2 * (eni + boyi)
def yuza(eni, boyi):
    return eni * boyi
eni, boyi = input().split()
eni = int(eni)
boyi = int(boyi)
print(perimetr(eni, boyi))
print(yuza(eni, boyi))