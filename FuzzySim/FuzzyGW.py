import random

def fuzifikasi(Minimum, Maximum, nilai):
    if nilai <= Minimum:
        bawah = 1
        atas = 0
    elif nilai >= Maximum:
        bawah = 0
        atas = 1
    else:
        bawah = (Maximum - nilai) / (Maximum - Minimum)
        atas = (nilai - Minimum) / (Maximum - Minimum)
    return bawah, atas

def implikasi(arrinput):
    if arrinput[0] > arrinput[1]:
        hasil = arrinput[1]
    else:
        hasil = arrinput[0]
    return hasil 

def komposisi(arrinput):
    if arrinput[0] > arrinput[1]:
        hasil = arrinput[0]
    else:
        hasil = arrinput[1]
    return hasil

def defuzifikasi(BBz, BAz, lower, upper):
    atas = []
    bawah = []
    sumLow = 0
    sumUpp = 0
    for i in range(5):
        bawah.append(random.randint(BBz, BAz+1))
        sumLow += bawah[i]
        atas.append(random.randint(BBz, BAz+1))
        sumUpp += atas[i]
    hasil = round((((sumLow * lower)+(sumUpp * upper)) / ((len(bawah)*lower)+(len(atas)*upper))), 0)
    return bawah, atas, hasil