def narx_bilan(narx, soliq=12):
    return narx + narx * soliq // 100
narx = int(input())
soliq = int(input())
print(narx_bilan(narx))
print(narx_bilan(narx, soliq))
