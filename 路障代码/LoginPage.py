from tkinter import *
from tkinter.messagebox import *
from MainPage import *
from Register import *
from Connect import *



class LoginPage(object):
    def __init__(self, master=None):
        self.root = master #定义内部变量root
        self.root.geometry('%dx%d' % (400, 250)) #设置窗口大小
        self.root.resizable(width=False, height=False)
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root,height=400,width=300) #创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        #Label(self.page, text = '账 户: ').grid(row=6, stick=W, pady=40)
        Entry1 = Entry(self.page, textvariable=self.username,relief=GROOVE)
        Entry1.grid(row=6,pady=26)
        Entry1.insert(0,'电话')
        Entry1.config(fg = 'grey')
        #Label(self.page, text = '密 码: ').grid(row=7, stick=W, pady=10)
        Entry2= Entry(self.page, textvariable=self.password,fg = "gray",relief=GROOVE)#, show='*')
        Entry2.grid(row=7,pady=10)
        Entry2.insert(0,'密码')


        Button(self.page, text='登 录', command=self.loginCheck,width=20,bg='#32cd32',activebackground='#00fa9a',relief=GROOVE).grid(row=8,pady=10)
        Button(self.page, text = '注 册',command=self.registerMan,width=20,relief=GROOVE,activebackground='#a9a9a9').grid(row=9)



    def loginCheck(self):
        accout = self.username.get()
        secret = self.password.get()

        fetchone_sql = 'SELECT * FROM user WHERE phone = ? '
        data = accout
        conn = get_conn()
        x = fetchone(conn, fetchone_sql, data)

        fetchone_sqlx = 'SELECT * FROM user WHERE password = ? '
        datax = secret
        connx = get_conn()
        y = fetchone(connx, fetchone_sqlx, datax)

        if x and y:
            self.page.destroy()
            MainPage(self.root)
        else:
            showinfo(title='错误', message='账号或密码错误！')

    def registerMan(self):
        self.page.destroy()
        Register(self.root)
