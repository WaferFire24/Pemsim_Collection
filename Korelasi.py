def sigma1(inp):
    arr = []
    out = 0
    for x in range(n):
        arr.append(inp[x])
        out += arr[x]
    return out, arr

def sigma2(inpX, inpY):
    arr = []
    out = 0
    for x in range(n):
        arr.append((inpX[x] * inpY[x]))
        out += arr[x]
    return out, arr

def sigpow1(inp):
    arr = []
    out = 0
    for x in range(n):
        arr.append((inp[x] ** 2))
        out += arr[x]
    return out, arr

def cariHasil(inpX, inpY, inpN):
    Yi = sigma1(inpY)[0]
    Yi2= sigpow1(inpY)[0]
    Xi2= sigpow1(inpX)[0]
    Xi = sigma1(inpX)[0]
    XiYi = sigma2(inpX, inpY)[0]
    out = round(((inpN * XiYi) - (Xi * Yi)) / ((((inpN * Xi2) - (Xi ** 2)) * ((inpN * Yi2)-(Yi ** 2))) ** 0.5), 3)
    return out

def skalaguilford(inp):
    if (inp < 0.2) and (inp >= 0):
        skala = 'Sangat Lemah'
    elif (inp < 0.4) and (inp >= 0.2):
        skala = 'Lemah'
    elif (inp < 0.6) and (inp >= 0.4):
        skala = 'Sedang'
    elif (inp < 0.8) and (inp >= 0.6):
        skala = 'Kuat'
    elif (inp <= 1.0) and (inp >= 0.8):
        skala = 'Sangat Kuat'
    return skala
    
def inputdata():
    global n
    print('Masukkan nilai x')
    while True:
        entry = input('num : ')
        if entry == '':
            break
        try:
            x.append(int(entry))
        except:
            print("Angka tidak valid!")
    print('Masukkan nilai y')
    while True:
        entry = input('num : ')
        if entry == '':
            break
        try:
            y.append(int(entry))
        except:
            print("Angka tidak valid!")
    n = int(input('Masukkan jumlah angka : '))
    
#--Main Program--#
x = []
y = []
n = 0
inputdata()
print('====Kesimpulan====')
hasil = cariHasil(x,y,n)
print('Skala angka = ', hasil)
print('Skala Guilford =', skalaguilford(hasil))
print('Koefisien Determinasi =', (hasil ** 2)*100,'%')
print('Terdapat', 100-((hasil ** 2)*100), '% kontribusi dari faktor lain')