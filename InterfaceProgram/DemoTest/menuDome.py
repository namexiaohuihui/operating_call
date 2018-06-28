# -*- coding: utf-8 -*- 
"""
@__author__ :DingDong
@file: NewMenuDome.py
@time: 2018/6/26 10:35
@Entry Name:operating
创建一个简易的菜单框，里面设置按钮
"""
import os
from tkinter import *
from tkinter.messagebox import *
class NewMenuDemo(Frame):
    def __init__(self,parent = None):
        Frame.__init__(self,parent)
        self.pack(expand = YES ,fill = BOTH) # 缺少这个之后，除菜单以外的书都不会显示
        self.createWidgets()
        self.master.title('标题测试框')
        self.master.iconname("tkPython")

    def createWidgets(self):
        self.makeMenuBar()
        self.makeToolBar()
        # lf = Label(self,text = '菜单添加标题测试')
        # lf.config(relief=SUNKEN,width = 40,height = 10,bg = 'white')
        # lf.pack(expand = YES,fill = BOTH)
        filedas = ('name','mima','lujing','dongzuo')

        self.entrie = []
        for field in filedas:
            row = Frame(self)
            lab = Label(row,width = 8,text = field)
            ent = Entry(row)
            row.pack(side=TOP,fill =X)
            lab.pack(side = LEFT)
            ent.pack(side=RIGHT,expand=YES,fill=X)
            self.entrie.append(ent)
        self.bind('<Return>',(lambda event : self.fetch(self.entrie)))


    def makeToolBar(self):
        toolbar = Frame(self,cursor = 'hand2',relief = SUNKEN , bd =2)
        toolbar.pack(side = BOTTOM,fill = X)
        Button(toolbar,text = 'Quit',command = self.menuQuit).pack(side=RIGHT)
        # Button(toolbar,text = 'Hello' , command = self.greeting).pack(side = LEFT)
        Button(toolbar,text = 'Hello' , command = (lambda : self.fetch(self.entrie))).pack(side = LEFT)
        print("运行了吗")

    def makeMenuBar(self):
        self.menubar = Menu(self.master)
        self.master.config(menu = self.menubar)
        self.fileMenu()
        self.editMenu()
        self.imageMenu()

    def fileMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label = 'OPen..',command = self.notdone)
        pulldown.add_command(label = 'Quit',command = self.menuQuit)
        self.menubar.add_cascade(label = 'File' , underline = 0,menu=pulldown)

    def editMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label = 'Paste',command = self.notdone)
        pulldown.add_command(label = 'Spam' , command = self.greeting)

        pulldown.add_separator() #下划线

        pulldown.add_command(label = 'Delect',command = self.greeting)
        pulldown.entryconfig(4,state = DISABLED) # 设置这个之后表明上一个添加的label无法点击
        self.menubar.add_cascade(label = 'Edit',underline = 0 , menu =pulldown)

    def imageMenu(self):
        '''
        PhotoImage对象被保存为列表，这与其他组件不同。
        如果不保存，内容就不复存在。（Python编程第八章有介绍）
        :return:
        '''
        # photoFiles = ('ameng.gif','fengc.gif')
        photoFiles = ('开关.png','日记.png','星球.png')
        # photoFiles = ('tupian.png')
        pulldown = Menu(self.menubar)
        self.photoObjs = []
        CUR_PATH = os.path.dirname(os.path.realpath(__file__))
        for filename in photoFiles:
            case_path = os.path.join(os.path.join(CUR_PATH, 'gifs'), filename)
            img = PhotoImage(file =case_path)
            # img = PhotoImage(filename) # 错误的
            pulldown.add_command(image = img,command = self.notdone)
            self.photoObjs.append(img)
        self.menubar.add_cascade(label='Image',underline = 0,menu = pulldown)


    def greeting(self):
        showinfo('或得','啥玩意')

    def notdone(self):
        showerror('没找到信息','你这是干嘛')

    def menuQuit(self):
        if askyesno('确定退出','你确定要退出吗?'):
            Frame.quit(self)
    def fetch(self,entries):
        for entry in entries:
            print('Input = "%s"' % entry.get())
if __name__ == '__main__':
    NewMenuDemo().mainloop() #TK运行必须调用该函数，不然不显示界面