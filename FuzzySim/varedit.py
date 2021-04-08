import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QFileDialog, QTableWidgetItem
from PyQt5.uic import loadUi
import index
#datamasuk = index.Hasilnya

class FuzzyDialog(QMainWindow):
    def __init__(self):
        super(FuzzyDialog, self).__init__()
        loadUi('UI/varpage.ui',self)
        #self.btnOpen.clicked.connect(self.Open)
        #self.btnNew.clicked.connect()
        #print('data masuk: ',datamasuk)  
        #self.Tabel1.setItem(0,0,QTableWidgetItem('OKE'))
        #self.writeTabel()

    def writeTabel(self,datanya):
        pass
        for i in range(6):
            for j in range(1,4):
                self.Tabel1.setItem(0,i,QTableWidgetItem(datanya[i]))
                datanya.pop(0)
        """
        header = ['Tipe', 'Variabel', 'Batas Atas', 'Nilai Batas Atas', 'Batas Bawah', 'Nilai Batas Bawah']
        for i in range(len(header)):
            #self.e = Entry(root, width=20, fg='black', font=('Arial',16,'bold'))
            self.Tabel1.setItem(0,i,QTableWidgetItem(header[i]))
        """

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FuzzyDialog()
    ex.setWindowTitle('')
    ex.show()
    sys.exit(app.exec_())