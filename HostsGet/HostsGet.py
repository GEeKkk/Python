import os
from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def Spider():
        html = requests.get("https://raw.githubusercontent.com/wangchunming/2017hosts/master/hosts-pc")
        with open('hosts', 'w', encoding='utf-8') as f:
            f.write(html.text)
        BsObj = BeautifulSoup(html.text)
        text.configure(state='normal')
        text.delete('1.0',END)
        text.insert('2.0',BsObj.get_text())
        text.configure(state='disabled')

def WriteIn():
        os.system('root.bat')

window = Tk()
flag1 = True
flag2 = False
window.resizable(width=flag2, height=flag1)
window.title("ForHosts")
window.geometry("900x600")
window.configure(bg='#47D8B5')
window.attributes("-alpha",0.95)

btn = Button(window, text='获取Hosts', command=Spider,bg='blue',relief=GROOVE,fg='white')
btn.place(x = 200, y = 50, height = 61, width = 100)

btn2 = Button(window, text='写入Hosts', command=WriteIn,bg='blue',relief=GROOVE,fg='white')
btn2.place(x = 600, y = 50, height = 61, width = 100)

text = Text(window)
text.configure(font='微软雅黑')
text.place(x = 0, y = 150, height = 450, width = 900)

window.mainloop()