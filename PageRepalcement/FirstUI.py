# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PageReplacement import *
from secondUI import *
import BornSrand
import random
import copy

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1007, 632)
        
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        MainWindow.setWindowIcon(QIcon('deer.png'))
       

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)


        MainWindow.style = """
                QPushButton{
                    background-color:rgba(0,0,0,0);
                }
                #SrandBtn { background-color: #3498db; border-radius: 5px; color: black; }
                #SrandBtn:hover { background-color:#2980b9; color: white}
                #DemoBtn { background-color: #58d68d; border-radius: 6px; color: black;}
                #DemoBtn:hover { background-color:#27ae60; color: white}
            """
        MainWindow.setStyleSheet(MainWindow.style)

        self.copyrightLbl = QLabel(self.centralwidget)
        copyfont = QFont("Microsoft YaHei",10,QFont.Normal)
        self.copyrightLbl.setFont(copyfont)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.addPermanentWidget(self.copyrightLbl)
        MainWindow.setStatusBar(self.statusbar)

        self.Memlcd = QLCDNumber(self.centralwidget)
        self.Memlcd.setGeometry(QRect(290, 360, 241, 201))
        self.Memlcd.setProperty("value", 4.0)
        self.Memlcd.setStyleSheet("border-radius:5px;""border-color: rgb(0, 0, 0);""border-style: solid;""border-width: 1px;")

       
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QRect(290, 580, 701, 31))
        self.horizontalSlider.setMinimum(4)
        self.horizontalSlider.setMaximum(32)
        self.horizontalSlider.valueChanged.connect(self.Memlcd.display)
        self.horizontalSlider.valueChanged.connect(self.Show)
        self.horizontalSlider.setVisible(False)
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {"
"border: 1px solid #4A708B;"
"background: #C0C0C0;"
"height: 3px;"
"border-radius: 2px;"
"padding-left:-1px;"
"padding-right:-1px;"
"}"

"QSlider::sub-page:horizontal {  "
"background: qlineargradient(x1:0, y1:0, x2:0, y2:1,"
"stop:0 #B1B1B1, stop:1 #c4c4c4);"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,"
"stop: 0 #5DCCFF, stop: 1 #1874CD);"
"border: 1px solid #4A708B;"
"height: 10px;"
"border-radius: 2px;"
"}"

"QSlider::add-page:horizontal {"
"background: #575757;"
"border: 0px solid #777;"
"height: 10px;"
"border-radius: 2px;"
"}"

"QSlider::handle:horizontal"
"{  "
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,   "
"stop:0.6 #45ADED, stop:0.778409 rgba(255, 255, 255, 255));  "

"width: 11px;"
"margin-top: -3px;"
"margin-bottom: -3px;"
"border-radius: 5px;"
"}"

"QSlider::handle:horizontal:hover{"
"background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 #2A8BDA,   "
"stop:0.778409 rgba(255, 255, 255, 255));  "

"width: 11px;"
"margin-top: -3px;"
"margin-bottom: -3px;"
"border-radius: 5px;"
"}"

"QSlider::sub-page:horizontal:disabled {"
"background: #00009C;"
"border-color: #999;"
"}"

"QSlider::add-page:horizontal:disabled {"
"background: #eee;"
"border-color: #999;"
"}"

"QSlider::handle:horizontal:disabled {"
"background: #eee;"
"border: 1px solid #aaa;"
"border-radius: 4px;"
"}")
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.HitRateLbl = QLabel(self.centralwidget)
        self.HitRateLbl.setGeometry(QRect(290, 10, 701, 51))
        self.HitRateLbl.setStyleSheet(
"font: 75 20pt \"微软雅黑\";"
"border-width: 1px; "
"border-color: rgb(204, 204, 204);"
"border-style: solid;"
"background-color: #bdc3c7;")


        self.FIFOlcd = QLCDNumber(self.centralwidget)
        self.FIFOlcd.setGeometry(QRect(290, 70, 151, 151))
        self.FIFOlcd.setStyleSheet("border-radius:5px;""border-color: rgb(170, 170, 255);""border-style: solid;""border-width: 1px;")

        self.LRUlcd = QLCDNumber(self.centralwidget)
        self.LRUlcd.setGeometry(QRect(470, 70, 151, 151))
        self.LRUlcd.setStyleSheet("border-radius:5px;"
"border-color: rgb(170, 170, 255);"
"border-style: solid;"
"border-width: 1px;")

        self.OPTlcd = QLCDNumber(self.centralwidget)
        self.OPTlcd.setGeometry(QRect(660, 70, 151, 151))
        self.OPTlcd.setStyleSheet("border-radius:5px;"
"border-color: rgb(170, 170, 255);"
"border-style: solid;"
"border-width: 1px;")

        self.LFUlcd = QLCDNumber(self.centralwidget)
        self.LFUlcd.setGeometry(QRect(840, 70, 151, 151))
        self.LFUlcd.setStyleSheet("border-radius:5px;"
"border-color: rgb(170, 170, 255);"
"border-style: solid;"
"border-width: 1px;")


        self.FIFOLbl = QLabel(self.centralwidget)
        self.FIFOLbl.setGeometry(QRect(290, 230, 151, 51))
        self.FIFOLbl.setStyleSheet("border-radius:5px;"
"font: 75 20pt \"微软雅黑\";"
"background-color: #bdc3c7;")
        self.FIFOLbl.setAlignment(Qt.AlignCenter)

        self.LRULbl = QLabel(self.centralwidget)
        self.LRULbl.setGeometry(QRect(470, 230, 151, 51))
        self.LRULbl.setStyleSheet("border-radius:5px;"
"font: 75 20pt \"微软雅黑\";"
"background-color: #bdc3c7;")
        self.LRULbl.setAlignment(Qt.AlignCenter)

        self.OPTLbl = QLabel(self.centralwidget)
        self.OPTLbl.setGeometry(QRect(660, 230, 151, 51))
        self.OPTLbl.setStyleSheet("border-radius:5px;"
"font: 75 20pt \"微软雅黑\";"
"background-color: #bdc3c7;")
        self.OPTLbl.setAlignment(Qt.AlignCenter)

        self.LFULbl = QLabel(self.centralwidget)
        self.LFULbl.setGeometry(QRect(840, 230, 151, 51))
        self.LFULbl.setStyleSheet("border-radius:5px;"
"font: 75 20pt \"微软雅黑\";"
"background-color: #bdc3c7;")
        self.LFULbl.setAlignment(Qt.AlignCenter)

        self.MemLbl = QLabel(self.centralwidget)
        self.MemLbl.setGeometry(QRect(290, 300, 701, 51))
        self.MemLbl.setStyleSheet("font: 75 20pt \"微软雅黑\";"
        "background-color: #bdc3c7;"
        "border-width: 1px;"
        "border-color: rgb(204, 204, 204);"
        "border-style: solid;")

        self.RefLbl = QLabel(self.centralwidget)
        self.RefLbl.setGeometry(QRect(550, 360, 441, 110))
        self.RefLbl.setOpenExternalLinks(True)
        self.RefLbl.setStyleSheet("border-radius:5px;""font: 50 12pt \"微软雅黑\";""border-width: 1px;""border-style: solid;")
        self.RefLbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.AboutLbl = QLabel(self.centralwidget)
        self.AboutLbl.setGeometry(QRect(550, 480, 441, 30))
        self.AboutLbl.setStyleSheet("border-radius:5px;""font: 50 12pt \"微软雅黑\";""border-width: 1px;""border-style: solid;")
        self.AboutLbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)


        #SrandButton
        self.SrandBtn = QPushButton(self.centralwidget)
        self.SrandBtn.setGeometry(QRect(20, 570, 251, 38))
        self.SrandBtn.clicked.connect(self.FillInTable)
        self.SrandBtn.clicked.connect(self.Show)
        self.SrandBtn.clicked.connect(self.Visible)
        self.SrandBtn.setObjectName('SrandBtn')
        Sfont = QFont("Microsoft YaHei",15,QFont.Normal)
        self.SrandBtn.setFont(Sfont)
      

        self.DemoBtn = QPushButton(self.centralwidget)
        self.DemoBtn.clicked.connect(self.SecondUI)#!!!!!!!!!!!!!!!!!!!!!!!!
        self.DemoBtn.setGeometry(QRect(550, 518, 441, 42))
        self.DemoBtn.setVisible(False)
        self.DemoBtn.setObjectName('DemoBtn')
        Dfont = QFont("Microsoft YaHei",15,QFont.Normal)
        self.DemoBtn.setFont(Dfont)


        #Form
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QRect(20, 10, 253, 551))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(320)
        self.tableWidget.setColumnWidth(0, 102)
        self.tableWidget.setColumnWidth(1, 102)
        self.tableWidget.setHorizontalHeaderLabels(["随机数", "页地址"])
        Tfont = QFont("Microsoft YaHei",10,QFont.Normal)
        self.tableWidget.setFont(Tfont)
        self.tableWidget.setStyleSheet("border-radius:1px;"
"border-width: 1px; "
"border-color: rgb(204, 204, 204);"
"border-style: solid;")
        self.tableWidget.setGridStyle(Qt.SolidLine)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def FillInTable(self):
        global AddrStream
        SrandNum = [random.randint(0, 319) for i in range(320)]
        AddrStream = [int(content/10) for content in SrandNum]
        BornSrand.SetSrandValue(SrandNum)
        BornSrand.SetAddrValue(AddrStream)

        for index in range(0,320):
            itemZ = QTableWidgetItem(str(SrandNum[index]))
            itemZ.setTextAlignment(Qt.AlignCenter)
            itemO = QTableWidgetItem(str(AddrStream[index]))
            itemO.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(index,0,itemZ)
            self.tableWidget.setItem(index,1,itemO)
    
    def Show(self):
        global AddrStream
        BornSrand.SetSliderValue(self.horizontalSlider.value())
        Ago = PageReplacement(AddrStream)
        self.FIFOlcd.display(Ago.FIFO())
        self.LRUlcd.display(Ago.LRU())
        self.OPTlcd.display(Ago.OPT())
        self.LFUlcd.display(Ago.LFU())
    
    def Visible(self):
        self.horizontalSlider.setVisible(True)
        self.DemoBtn.setVisible(True)

    def SecondUI(self):
        self.secondwin = Modal_Ui()
        self.secondwin.initUI()

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "页面置换算法模拟"))
        self.SrandBtn.setText(_translate("MainWindow", "随机数"))
        self.DemoBtn.setText(_translate("MainWindow", "演 示"))
        self.AboutLbl.setText(_translate("MainWindow", "小组成员: 李静润 许春林 胡远智 鲁 健"))
        self.HitRateLbl.setText(_translate("MainWindow", " 命中率"))
        self.FIFOLbl.setText(_translate("MainWindow", "FIFO"))
        self.LRULbl.setText(_translate("MainWindow", "LRU"))
        self.OPTLbl.setText(_translate("MainWindow", "OPT"))
        self.LFULbl.setText(_translate("MainWindow", "LFU"))
        self.MemLbl.setText(_translate("MainWindow", " 物理块数"))
        self.RefLbl.setText(_translate("MainWindow", "<html><head/><body><p>参考链接:</p><p><a href=\"http://code.py40.com/2182.html\">code.py40.com/2182.html</a></p><p><a href=\"http://www.qtcn.org/bbs/read-htm-tid-7687.html\">http://www.qtcn.org/bbs/read-htm-tid-7687.html</a></p></body></html>"))
        self.copyrightLbl.setText(_translate("MainWindow", "Copyright (c) 2018 P.L."))


'''
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''

