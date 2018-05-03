#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import BornSrand


class Modal_Ui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #self.setGeometry(300, 200, 1200, 340)
        self.resize(927, 467) 
        self.setWindowTitle('演示') 
        self.setObjectName("window")
        self.setWindowIcon(QIcon('loading.png'))
        self.setWindowModality(Qt.ApplicationModal)

        self.gridLayout = QGridLayout(self)

       
        self.DzTable = QTableWidget(self)
        #self.DzTable.setGeometry(QRect(0, 0, 1000, 80)
        self.DzTable.setMaximumSize(QSize(16777215, 80))
        self.DzTable.setColumnCount(320)
        self.DzTable.setRowCount(2)

        for i in range(0,320):
            self.DzTable.setColumnWidth(i, 30)

        self.DzTable.setVerticalHeaderLabels(["随机数", "页地址"])
        self.DzTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.DzTable.horizontalHeader().setVisible(False)
       
        SrandNum_s = BornSrand.GetSrandValue()
        AddrStream_s = BornSrand.GetAddrValue()

        for index in range(0,320):
            itemZ = QTableWidgetItem(str(SrandNum_s[index]))
            itemZ.setTextAlignment(Qt.AlignCenter)
            itemO = QTableWidgetItem(str(AddrStream_s[index]))
            itemO.setTextAlignment(Qt.AlignCenter)
            self.DzTable.setItem(0,index,itemZ)
            self.DzTable.setItem(1,index,itemO)

        self.tabWidget = QTabWidget(self)

        global ColumnCount
        ColumnCount = BornSrand.GetSliderValue()
        GetFifo = BornSrand.GetFifo()
        GetLru = BornSrand.GetLru()
        GetOpt = BornSrand.GetOpt()
        GetLfu = BornSrand.GetLfu()

        #print(GetFifo)
        #print(len(GetFifo))

        '''
        print(GetLru)


        print(len(GetLru))
        '''
        '''
        print(ColumnCount)
        '''

        self.FIFO = QTableWidget()
        self.FIFO.setColumnCount(ColumnCount+4)
        self.FIFO.setHorizontalHeaderLabels(['+']*ColumnCount+['命中','未命中次数','置入','置出'])
        for i in range(0,ColumnCount):
            self.FIFO.setColumnWidth(i, 30)
        #self.FIFO.setRowCount(320)
        self.FIFO.setRowCount(len(GetFifo))
        for index in range(0,len(GetFifo)):
            for indexMe in range(0,ColumnCount+4):
                item_P = QTableWidgetItem(str(GetFifo[index][indexMe]))
                self.FIFO.setItem(index,indexMe,item_P)
                item_P.setTextAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.FIFO, "FIFO")

        self.LRU = QTableWidget()
        self.LRU.setColumnCount(ColumnCount+4)
        self.LRU.setHorizontalHeaderLabels(['+']*ColumnCount+['命中','未命中次数','置入','置出'])
        for ii in range(0,ColumnCount):
            self.LRU.setColumnWidth(ii, 30)
        self.LRU.setRowCount(len(GetLru))
        for indexu in range(0,len(GetLru)):
            for indexMeu in range(0,ColumnCount+4):
                item_PP = QTableWidgetItem(str(GetLru[indexu][indexMeu]))
                self.LRU.setItem(indexu,indexMeu,item_PP)
                item_PP.setTextAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.LRU, "LRU")

        self.OPT = QTableWidget()
        self.OPT.setColumnCount(ColumnCount+4)
        self.OPT.setHorizontalHeaderLabels(['+']*ColumnCount+['命中','未命中次数','置入','置出'])
        for iii in range(0,ColumnCount):
            self.OPT.setColumnWidth(iii, 30)
        self.OPT.setRowCount(len(GetOpt))
        for indexuu in range(0,len(GetOpt)):
            for indexMeuu in range(0,ColumnCount+4):
                item_PPP = QTableWidgetItem(str(GetOpt[indexuu][indexMeuu]))
                self.OPT.setItem(indexuu,indexMeuu,item_PPP)
                item_PPP.setTextAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.OPT, "OPT")

        
        self.LFU = QTableWidget()
        self.LFU.setColumnCount(ColumnCount+4)
        self.LFU.setHorizontalHeaderLabels(['+']*ColumnCount+['命中','未命中次数','置入','置出'])
        for iiii in range(0,ColumnCount):
            self.LFU.setColumnWidth(iiii, 30)
        self.LFU.setRowCount(len(GetLfu))
        for indexuuu in range(0,len(GetLfu)):
            for indexMeuuu in range(0,ColumnCount+4):
                item_PPPP = QTableWidgetItem(str(GetLfu[indexuuu][indexMeuuu]))
                self.LFU.setItem(indexuuu,indexMeuuu,item_PPPP)
                item_PPPP.setTextAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.LFU, "LFU")
        

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.DzTable, 0, 0, 1, 1)

        

        self.show()

'''
class WorkThread(QThread):
    sinOut = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.m = 0

    def run(self):
        while self.m < 5:
            self.m += 1
            self.sinOut.emit(self.m)    #反馈信号出去
            time.sleep(1)
'''


'''
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Modal_Ui()
    ui.initUI()
    sys.exit(app.exec_())
'''