from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import re
import webbrowser

def Spider():
    url = var1.get()
    pattern = re.compile(r'av[0-9]*')
    matchResult = pattern.search(url)
    if not matchResult:
        messagebox.showinfo("警告", "输入非法!!!")
    html = requests.get("http://www.bilibili.com/video/"+url+'/')
    bsObj = BeautifulSoup(html.text)
    tagg = bsObj.findAll("", {"id":"bofqi"}) #'bofqi'什么鬼
    for ACDC in tagg:
        #Peak = ACDC.get_text().split("cid=")[1].split("&")[0]
        pat = re.compile(r'cid=(.+?)&')
        a = pat.findall(ACDC.get_text())
        Peak = "".join(a)                   #这里是比较难想的地方
    ahtml = requests.get("http://comment.bilibili.com/" + Peak + ".xml")
    BsObj = BeautifulSoup(ahtml.text)
    Lisst = BsObj.findAll("d")
    #with open('PeakFrist.txt', 'w', encoding='utf-8') as f:
    #f.write(ahtml.text)
        #f.write(BsObj.get_text())
    words = "弹幕共" + str(len(Lisst)) + "条"
    lbl2.config(text = words)
    #text2.insert('1.0',len(Lisst))
    text.insert('2.0',BsObj.get_text()+'\n')


def Ahu_notice():
    html = requests.get("http://jwc.ahu.cn/main/notice.asp").content.decode('gbk')
    bsObj = BeautifulSoup(html)
    tagg = bsObj.findAll('a', href=re.compile("^(show)\.asp\?id\=[0-9]*"))
    for link in tagg:
        if 'href' in link.attrs:
            text.insert('1.0', link.get_text()+'\n')
            text.insert('2.0', 'http://jwc.ahu.cn/main/'+link.attrs['href']+'\n\n')


def Search():
    urll = var2.get()
    '''
    pattern = re.compile(r'av[0-9]*')
    matchResult = pattern.search(url)
    if not matchResult:
        messagebox.showinfo("警告", "输入非法!!!")
    '''
    webbrowser.open_new(urll)

window = Tk()
window.resizable(width=False, height=False)
window.title("webHydra")
window.geometry("900x600")
#img1 = PhotoImage(file='lu.ico')
#window.tk.call('wm', 'iconphoto',window._w, img1)
window.wm_iconbitmap('lu.ico')
#window.configure(background='#4c66a4')

lbl = Label(window, text="视频番号:")
lbl.place(x = 10, y = 10)


lbl2 = Label(window)
lbl2.place(x = 10,y = 40)
'''
filename = '2.png'
img = PhotoImage(file=filename)
lal3 = Label(window, image=img)
lal3.place(x = 500, y = 80)
'''

lbl4 = Label(window, text = "输入网址:")
lbl4.place(x = 500, y = 80)

var1=StringVar()
ent = Entry(window, textvariable=var1)
ent.place(x = 70, y = 10, width = 150, height = 25)
var1.set("")

var2=StringVar()
ent2 = Entry(window, textvariable=var2)
ent2.place(x = 560, y = 80, width = 220, height = 25)
var2.set("")

btn = Button(window, text='GO', command=Spider)
btn.place(x = 240, y = 10, height = 25, width = 50)

btn2 = Button(window, text='安大教务处公告',command=Ahu_notice)
btn2.place(x = 500, y = 10, height = 25, width = 90)

btn3 = Button(window, text='查看',command=Search)
btn3.place(x = 790, y = 80, height = 25, width = 50)

text = Text(window)
text.place(x = 10, y = 80, height = 500, width = 480)

#text2 = Text(window)
#text2.place(x = 70, y = 40, height = 20, width = 30)
#lbl.pack()
#ent.pack()
#btn.pack()
#text.pack()
window.mainloop()