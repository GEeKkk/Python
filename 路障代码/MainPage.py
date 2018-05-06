from tkinter import *
from view import *  #菜单栏对应的各个子页面

class MainPage(object):
    def __init__(self, master=None):
        self.root = master #定义内部变量root
        self.root.geometry('%dx%d' % (1500, 700)) #设置窗口大小
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root) # 创建不同Frame
        self.blockPage = QueryFrame(self.root)
        self.workPage = WorkFrame(self.root)
        self.modifyPage = ModifyFrame(self.root)
        self.inputPage.pack() #默认显示数据录入界面
        menubar = Menu(self.root)
        menubar.add_command(label='报告路障', command = self.inputData)
        menubar.add_command(label='路障查询', command = self.blockData)
        menubar.add_command(label='施工查询', command = self.workData)
        menubar.add_command(label='修改路障信息', command = self.modifyDisp)
        self.root['menu'] = menubar  # 设置菜单栏

    def inputData(self):
        self.inputPage.pack()
        self.blockPage.pack_forget()
        self.workPage.pack_forget()
        self.modifyPage.pack_forget()

    def blockData(self):
        self.inputPage.pack_forget()
        self.blockPage.pack()
        self.workPage.pack_forget()
        self.modifyPage.pack_forget()

    def workData(self):
        self.inputPage.pack_forget()
        self.blockPage.pack_forget()
        self.workPage.pack()
        self.modifyPage.pack_forget()

    def modifyDisp(self):
        self.inputPage.pack_forget()
        self.blockPage.pack_forget()
        self.workPage.pack_forget()
        self.modifyPage.pack()