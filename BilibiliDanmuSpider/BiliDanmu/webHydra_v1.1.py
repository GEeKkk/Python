'''
@Author:                PeakLu 
@Date:                  2017-04-23
@Last Modified by:      PeakLu 
@Last Modified time:    2017-05-30
@DevelopTool:           Visual Studio Code
@Python:                v3.5.0
Based on                Win10 64bit
'''

from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import re
import webbrowser

###################################################################
#定义函数
def Spider():
    url = var1.get()
    pattern = re.compile(r'av[0-9]*')#对输入内容进行判断
    matchResult = pattern.search(url)
    if not matchResult:
        messagebox.showinfo("警告", "输入非法!!!")
    else:
        try:
            html = requests.get("http://www.bilibili.com/video/"+url+'/')
            html.raise_for_status()
        except requests.RequestException as e:
            text.configure(state='normal')
            text.delete('1.0',END)
            text.insert('1.0',"老铁，视频被徐逸删了..."+'\n')
            text.configure(state='disabled')
        else:
            bsObj = BeautifulSoup(html.text)
            tagg = bsObj.findAll("", {"id":"bofqi"})#这个bofqi不知道是什么鬼,反正能用就行
            for ACDC in tagg:#找视频id
                pat = re.compile(r'cid=(.+?)&')
                a = pat.findall(ACDC.get_text())
                Peak = "".join(a)
            try:
                ahtml = requests.get("http://comment.bilibili.com/" + Peak + ".xml")
            except UnboundLocalError:#异常处理
                text.configure(state='normal')
                text.delete('1.0',END)
                text.insert('1.0',"该视频不存在！"+'\n')
                text.configure(state='disabled')
            BsObj = BeautifulSoup(ahtml.text)
            Lisst = BsObj.findAll("d")
            words = "弹幕共" + str(len(Lisst)) + "条"
            lbl2.config(text = words)
            text.configure(state='normal')
            text.delete('1.0',END)
            text.insert('2.0',BsObj.get_text()+'\n')
            text.configure(state='disabled')

def Ahu_notice():
    html = requests.get("http://jwc.ahu.cn/main/notice.asp").content.decode('gbk')
    bsObj = BeautifulSoup(html)
    tagg = bsObj.findAll('a', href=re.compile("^(show)\.asp\?id\=[0-9]*"))
    text.delete('1.0',END)
    for link in tagg:
        if 'href' in link.attrs:
            text.configure(state='normal')
            text.insert('1.0', link.get_text()+'\n')
            text.insert('2.0', 'http://jwc.ahu.cn/main/'+link.attrs['href']+'\n\n')
    text.configure(state='disabled')   
    '''
    try:   
        html = requests.get("http://jwc.ahu.cn/main/notice.asp").content.decode('gbk')
        html.raise_for_status()
    except requests.RequestException as e:
        text.insert('1.0',"教务处主页已挂...!!@_@"+'\n')
    else:
        bsObj = BeautifulSoup(html)
        tagg = bsObj.findAll('a', href=re.compile("^(show)\.asp\?id\=[0-9]*"))
        for link in tagg:
            if 'href' in link.attrs:
                text.insert('1.0', link.get_text()+'\n')
                text.insert('2.0', 'http://jwc.ahu.cn/main/'+link.attrs['href']+'\n\n')
    '''
    #上面这段异常处理是在当时教务处网站挂掉的情况下写的，当时可以使用，现在测试无法使用....||-_-

def Search():
    urll = var2.get()
    if not urll:
        messagebox.showinfo("警告", "输入非法!!!")
    else:
        webbrowser.open_new(urll)

##########################################################################
#定义窗口
window = Tk()
flag1 = True
flag2 = False
window.resizable(width=flag2, height=flag1)
#window.resizable(width=True, height=True)
window.title("webHydra")
window.geometry("900x600")
window.configure(bg='#47D8B5')
window.attributes("-alpha",0.95)
window.wm_iconbitmap('lu.ico')

lbl = Label(window, text="视频番号:",bg='#47D8B5',fg='black')
lbl.place(x = 10, y = 10)

lbl2 = Label(window,bg='#47D8B5',fg='black')
lbl2.place(x = 10,y = 40)

lbl4 = Label(window, text = "复制网址:",bg='#47D8B5',fg='black')
lbl4.place(x = 10, y = 120)

var1=StringVar()
ent = Entry(window, textvariable=var1)
ent.place(x = 70, y = 10, width = 150, height = 25)
var1.set("")

var2=StringVar()
ent2 = Entry(window, textvariable=var2)
ent2.place(x = 70, y = 120, width = 150, height = 25)
var2.set("")

btn = Button(window, text='GO', command=Spider,bg='blue',relief=GROOVE,fg='white')
btn.place(x = 220, y = 10, height = 25, width = 50)

btn2 = Button(window, text='安大教务处公告',command=Ahu_notice,bg='blue',relief=GROOVE,fg='white')
btn2.place(x = 10, y = 70, height = 25, width = 90)

btn3 = Button(window, text='查看',command=Search,bg='blue',relief=GROOVE,fg='white')
btn3.place(x = 220, y = 120, height = 25, width = 50)

text = Text(window)
text.configure(font='微软雅黑')
text.place(x = 0, y = 150, height = 450, width = 900)

window.mainloop()