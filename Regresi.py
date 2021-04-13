#INI ADALAH PROGRAM MENGHITUNG REGRESI#
#Nama : Akram Muhammad Nuramadhan
#NRP : 152018095
#-----------------------------------------#
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

def cariA(inpX, inpY, inpN):
    Yi = sigma1(inpY)[0]
    Xi2, nXi2 = sigpow1(inpX)[:2]
    Xi = sigma1(inpX)[0]
    XiYi = sigma2(inpX, inpY)[0]
    out = []
    for x in range(n):
        out.append(round(((Yi * Xi2) - (Xi * XiYi)) / ((inpN * nXi2[x]) - (Xi ** 2)), 3))
    return out

def cariB(inpX, inpY, inpN):
    Yi = sigma1(inpY)[0]
    Xi = sigma1(inpX)[0]
    XiYi = sigma2(inpX, inpY)[0]
    out = []
    for x in range(n):
        out.append(round(((inpN * XiYi) - (Xi * Yi)) / ((inpN * Xi) - (Xi ** 2)), 3))
    return out

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
    n = int(input('nilai n : '))


'''__MAIN PROGRAM__'''
x = []
y = []
n = 0
inputdata()
a = cariA(x,y,n)
b = cariB(x,y,n)
print('Nilai a (konstatnta) = ', a)
print('Nilai b (koefisien) = ', b)
print('===Persamaan===')
for i in range(n):
    print('(', i+1 ,') Y = ', a[i], ' + (', b[i], ')x')