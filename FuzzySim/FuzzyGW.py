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