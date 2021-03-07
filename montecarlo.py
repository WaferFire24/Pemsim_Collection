#INI ADALAH PROGRAM SIMULASI MONTECARLO#
#Nama : Akram Muhammad Nuramadhan
#NRP : 152018095
#-----------------------------------------#
import random
def inputdata():
    while True:
        entry1 = input('Demand(s) = ')
        entry2 = input('weeks : ')
        if (entry1 == '') and (entry1 == ''):
                break
        try:
            datainput.append((int(entry1),int(entry2)))
        except:
            print("Masukkan Tidak Valid!")

def prob():
    ftot = 0
    out = []
    for x in range(len(datainput)):
        ftot += datainput[x][1]
    for x in range(len(datainput)):
        n = datainput[x][1] / ftot
        out.append(n)
    return out

def probkum(inprob):
    out = []
    out.append(inprob[0])
    panjang = len(inprob) - 1
    for x in range(panjang):
        n = out[x] + inprob[x+1]
        out.append(round(n,1))
    return out

def interval(inprobkum):
    atas = []
    bawah = []
    bawah.append(0)
    for x in range((len(inprobkum))-1):
        n = inprobkum[x] + 0.001
        bawah.append(n)
    for x in range((len(inprobkum))):
        n = inprobkum[x]
        atas.append(n)
    return bawah, atas

def predict(banyaknya, bawah, atas, harga):
    total1 = 0
    total2 = 0
    data = []
    out = []
    for x in range(banyaknya):
        data.append(random.random())
    for x in range(banyaknya):
        if (data[x] >= bawah[0]) and (data[x] <= atas[0]):
            n=0
        elif (data[x] >= bawah[1]) and (data[x] <= atas[1]):
            n=1
        elif (data[x] >= bawah[2]) and (data[x] <= atas[2]):
            n=2
        elif (data[x] >= bawah[3]) and (data[x] <= atas[3]):
            n=3
        elif (data[x] >= bawah[4]) and (data[x] <= atas[4]):
            n=4
        out.append(n)
    data = []
    for x in  range(len(out)):
        total1 += out[x]
        n = out[x] * harga
        total2 += n
    print('Prediksi Permintaan Sebanyak = ', total1, 'pcs')
    print('Prediksi Pengeluaran = Rp.',total2)

datainput = []
inputdata()
alpha = prob()
beta = probkum(alpha)
bo, ab = interval(beta)[:2]
npredict = int(input('Masukkan banyak prediksi: '))
price = int(input('Tentukan modal barang: '))
print('== Prediksi Dengan MonteCarlo ==')
predict(npredict, bo, ab, price)