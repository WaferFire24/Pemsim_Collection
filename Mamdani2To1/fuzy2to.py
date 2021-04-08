import xlrd
#import numpy as np
#from tkinter import *

def Open():
    tipe = []
    var = []
    batas = []
    natas = []
    bbawah = []
    nbawah = []
    masukan = []
    book = xlrd.open_workbook('tes.xls')
    sheet = book.sheet_by_name("Sheet1")
    for i in range (2,5):
        tipe.append(sheet.cell(i,0).value)
        var.append(sheet.cell(i,1).value)
        batas.append(sheet.cell(i,2).value)
        natas.append(sheet.cell(i,3).value)
        bbawah.append(sheet.cell(i,4).value)
        nbawah.append(sheet.cell(i,5).value)
    hasilst = tipe + var + batas + natas + bbawah + nbawah
    return hasilst


class Table:
    def __init__(self,root):
        header = ['Tipe', 'Variabel', 'Batas Atas', 'Nilai BA.', 'Batas Bawah', 'Nilai BB.']
        for i in range(len(header)):
            self.e = Entry(root, width=20, fg='black',
                           font=('Arial',16,'bold'))
            self.e.grid(row=0, column=i)
            self.e.insert(END, header[i]) 
        for i in range(6):
            for j in range(1,4):
                self.e = Entry(root, width=20, fg='black',
                               font=('Arial',16,'bold'))
                self.e.grid(row=j, column=i)
                self.e.insert(END, lst[0])
                lst.pop(0)


lst = Open()
# create root window
root = Tk()
t = Table(root)
root.mainloop()
print(lst)
