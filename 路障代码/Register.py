from tkinter import *
from Connect import *
import sqlite3
import LoginPage
from tkinter.messagebox import *

class Register(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('400x350')
        self.root.resizable(width=False, height=False)
        self.Name = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.telnum = StringVar()
        self.address = StringVar()
        self.CreatePage()
    

    def CreatePage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page).grid()
        Label(self.page, text = '姓 名:',bg="#a1dbcd").grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.Name).grid(row=1, column=1, stick=E)
        Label(self.page, text = '邮 件:',bg="#a1dbcd").grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.email).grid(row=2, column=1, stick=E)
        Label(self.page, text = '密 码:',bg="#a1dbcd").grid(row=3, stick=W, pady=10)
        Entry(self.page, textvariable=self.password).grid(row=3, column=1, stick=E)
        Label(self.page, text = '电 话:',bg="#a1dbcd").grid(row=4, stick=W, pady=10)
        Entry(self.page, textvariable=self.telnum).grid(row=4, column=1, stick=E)
        Label(self.page, text = '地 址:',bg="#a1dbcd").grid(row=5, stick=W, pady=10)
        Entry(self.page, textvariable=self.address).grid(row=5, column=1, stick=E)
        Button(self.page, text = '保 存',command=self.Save,width=20,relief=GROOVE,bg='#1e90ff',activebackground='#00bfff').grid(row=7,column=1,pady=10)
        Button(self.page, text = '返 回',command=self.Return,width=20,relief=GROOVE,activebackground='#a9a9a9').grid(row=8,column=1)

    def Save(self):
        if self.Name.get() =='' or self.password.get()=='' or self.telnum.get()=='':
            showinfo(title='警告', message='姓名,密码,电话为必填项')
        else:
            save_sql = '''INSERT INTO user values (?, ?, ?, ?, ?)'''
            data = [(self.Name.get(), self.email.get(), self.password.get(), self.telnum.get(), self.address.get())]
            conn = get_conn()
            EX = save(conn, save_sql, data)
            if EX:
                self.page.destroy()
                LoginPage.LoginPage(self.root)
            else:
                showinfo(title='警告', message='帐号已存在')

    def Return(self):
        self.page.destroy()
        LoginPage.LoginPage(self.root)