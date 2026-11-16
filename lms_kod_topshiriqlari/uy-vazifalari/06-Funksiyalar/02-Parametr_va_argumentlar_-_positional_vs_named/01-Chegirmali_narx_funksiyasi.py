def chegirmali_narx(narx, foiz):
    chegirma = narx * foiz // 100
    return narx - chegirma
narx = int(input())
foiz = int(input())
print(chegirmali_narx(narx, foiz))