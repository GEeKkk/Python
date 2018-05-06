from tkinter import *
from tkinter.messagebox import *
import datetime
import random
from Connect import *
from tkinter import ttk
import webbrowser

class InputFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root
        self.address = StringVar()
        self.size = StringVar()
        self.location = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text = '路障地址:',bg="#a1dbcd").grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.address, width = 50).grid(row=1, column=1, stick=E)
        Label(self, text = '(将查询到的地址粘贴于此)',bg="#a1dbcd").grid(row=1, column=2)
        Label(self, text = '路障大小:',bg="#a1dbcd").grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.size, width = 50).grid(row=2, column=1, stick=E)
        Label(self, text = '路障位置:',bg="#a1dbcd").grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.location, width = 50).grid(row=3, column=1, stick=E)        
        Button(self, text='位置查询',command=self.Location, width = 50,height = 1,bg='#32cd32',activebackground='#00fa9a',relief=GROOVE).grid(row=6, column=1, stick=E, pady=10)
        Button(self, text='录  入',command=self.saveInfo, width = 50,height = 1,bg='#32cd32',activebackground='#00fa9a',relief=GROOVE).grid(row=7, column=1, stick=E, pady=10)


    def saveInfo(self):
        if self.address.get() =='' or self.size.get()=='' or self.location.get()=='':
            showinfo(title='警告', message='信息填写不完整')
        else:
            nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S");#生成当前时间
            randomNum=random.randint(0,100);#生成的随机整数n，其中0<=n<=100
            if randomNum<=10:
                randomNum=str(0)+str(randomNum)
            blockid=str(nowTime)+str(randomNum)

            Label(self, text = '路障标识: ',bg="#a1dbcd").grid(row=4, stick=W, pady=10)
            #Label(self, text=blockid,state='disabled').grid(row=4,column=1, stick=E, pady=10)
            w = Text(self, height=1, width=20, borderwidth=0)
            w.grid(row=4,column=1, stick=E, pady=10)
            w.insert(1.0, blockid)
            w.configure(state="disabled")

            save_sql = '''INSERT INTO blockinfo values (?, ?, ?, ?, ?)'''
            data = [(blockid, self.address.get(), self.size.get(), self.location.get(), 0)]
            conn = get_conn()
            save(conn, save_sql, data)
            
            save_sqll = '''INSERT INTO workcommand values (?,?,?,?,?,?,?)'''
            datal = [(blockid,'/',0,0,'/',0,0)]
            connl = get_conn()
            save(connl, save_sqll, datal)

            showinfo(title='提示', message='保存成功')

    def Location(self):
        webbrowser.open_new('http://chaipip.com/ip.php')

class QueryFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master #定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self, text='路障标识',bg="#a1dbcd").grid(row=2, column=1,padx=32,pady=5)
        Label(self, text='路障地址',bg="#a1dbcd").grid(row=2, column=2,padx=32,pady=5)
        Label(self, text='路障大小',bg="#a1dbcd").grid(row=2, column=3,padx=32,pady=5)
        Label(self, text='路障位置',bg="#a1dbcd").grid(row=2, column=4,padx=32,pady=5)
        Label(self, text='优先级',bg="#a1dbcd").grid(row=2, column=5,padx=32,pady=5)
        Button(self, text = '刷 新',command=self.refresh,relief=GROOVE).grid(row=2,column=0)
        fetchall_sql = '''SELECT * FROM blockinfo'''
        conn = get_conn()
        allin = fetchall(conn, fetchall_sql)
        if allin is None:
            pass
        else:
            for i in range(len(allin)):
                for j in range(5):
                    Label(self, text=allin[i][j], width=20).grid(row=3+i, column=1+j,padx=32)

    
    def refresh(self):
        fetchall_sql = '''SELECT * FROM blockinfo'''
        conn = get_conn()
        allin = fetchall(conn, fetchall_sql)
        if allin is None:
            pass
        else:
            for i in range(len(allin)):
                for j in range(5):
                    Label(self, text=allin[i][j], width=20).grid(row=3+i, column=1+j,padx=32)



class WorkFrame(Frame): # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master #定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self, text='路障标识',bg="#a1dbcd").grid(row=2, column=1,padx=32,pady=5)
        Label(self, text='施工队编号',bg="#a1dbcd").grid(row=2, column=2,padx=32,pady=5)
        Label(self, text='路障状态',bg="#a1dbcd").grid(row=2, column=3,padx=32,pady=5)
        Button(self, text = '刷 新',command=self.refresh,relief=GROOVE).grid(row=2,column=0)
        fetchall_sql = '''SELECT blockid,teamid,status FROM workcommand'''
        conn = get_conn()
        allin = fetchall(conn, fetchall_sql)
        if allin is None:
            pass
        else:
            for i in range(len(allin)):
                for j in range(3):
                    Label(self, text=allin[i][j]).grid(row=3+i, column=1+j,padx=32)

    def refresh(self):
        fetchall_sql = '''SELECT blockid,teamid,status FROM workcommand'''
        conn = get_conn()
        allin = fetchall(conn, fetchall_sql)
        if allin is None:
            pass
        else:
            for i in range(len(allin)):
                for j in range(3):
                    Label(self, text=allin[i][j]).grid(row=3+i, column=1+j,padx=32)




class ModifyFrame(Frame): 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.address = StringVar()
        self.size = StringVar()
        self.location = StringVar()
        self.id = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text = '路障地址:',bg="#a1dbcd").grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.address, width = 50).grid(row=1, column=1, stick=E)
        Label(self, text = '路障大小:',bg="#a1dbcd").grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.size, width = 50).grid(row=2, column=1, stick=E)
        Label(self, text = '路障位置:',bg="#a1dbcd").grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.location, width = 50).grid(row=3, column=1, stick=E)
        Label(self, text = '路障标识:',bg="#a1dbcd").grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.id, width = 50).grid(row=4, column=1, stick=E)
        Button(self, text='位置查询',command=self.Location, width = 50,height = 1,bg='#32cd32',activebackground='#00fa9a',relief=GROOVE).grid(row=6, column=1, stick=E, pady=10)
        Button(self, text='更 新',command=self.Update, width = 50,height = 1,bg='#32cd32',activebackground='#00fa9a',relief=GROOVE).grid(row=7, column=1, stick=E, pady=10)


    def Update(self):
        if self.address.get() =='' or self.size.get()=='' or self.location.get()=='' or self.id.get()=='':
            showinfo(title='警告', message='信息填写不完整')
        else:
            update_sql = 'UPDATE blockinfo SET blockadd = ?,size = ?, location = ? WHERE blockid = ? '
            data = [(self.address.get(), self.size.get(), self.location.get(), self.id.get())]
            conn = get_conn()
            update(conn, update_sql, data)
            

            showinfo(title='提示', message='保存成功')
    
    def Location(self):
        webbrowser.open_new('http://chaipip.com/ip.php')