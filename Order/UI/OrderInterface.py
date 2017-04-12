#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import Post.SendPost as ps
import webbrowser

url1='http://piao.ctrip.uat.qa.nt.ctripcorp.com/dest/t1829957.html'
url2='http://huodong.ctrip.uat.qa.nt.ctripcorp.com/activity/10000109.html'
url3='http://huodong.ctrip.uat.qa.nt.ctripcorp.com/activity/4128544.html'
url4='http://logging.uat.qa.nt.ctripcorp.com/;jsessionid=4F343A73436005191CC466430D5F249F;jsessionid=C911272C335D08C16AEA56A859FC8184;jsessionid=503B3F9866C56CFCEA3D049886634A6C#?as=7202'
ui=tk.Tk()
ui.title('Order UI')#add title

order=ttk.LabelFrame(ui,text="Order")
order.grid(column=0,row=1,padx=100,pady=100)#定义应用界面大小
test=ttk.LabelFrame(ui,text='test')
test.grid(column=0,row=0,padx=10,pady=10)

#-------------------------------------------------------------------
def orderLink():
    lable1=ttk.Button(test,text='门票',width=20,command=openUrl1)
    lable1.grid(column=0, row=0)
    lable2 = ttk.Button(test, text='玩乐',width=20,command=openUrl2)
    lable2.grid(column=1, row=0)
    lable3 = ttk.Button(test, text='wifi', width=20, command=openUrl3)
    lable3.grid(column=0, row=1)
    lable4 = ttk.Button(test, text='job', width=20, command=openUrl4)
    lable4.grid(column=1, row=1)
def openUrl1():
    webbrowser.open(url1,new=0)
def openUrl2():
    webbrowser.open(url2,new=0)
def openUrl3():
    webbrowser.open(url3,new=0)
def openUrl4():
    webbrowser.open(url4,new=0)
#----------------------------------------------------------------------
#alabel=ttk.Label(order,text="test")u
#点击按钮的事件
def clickNormal():
    if normal[0]:
        normal[1].insert(0,ps.sendNormalPost())

def vbkAOrder():
    if vbkAOrder[0]:
        vbkAOrder[1].insert(0,ps.sendAutoVBKPost())

def vbkMOrder():
    if vbkMOrder[0]:
        vbkMOrder[1].insert(0,ps.sendManVBKPost())

def DJOrder():
    if djOrder[0]:
        djOrder[1].insert(0,ps.sendDJdata())

#----------------------------------------------------------------------
#整体布局
def layOut(text,column1,column2,row1,row2,cn):
    actionNormal = ttk.Button(order, width=10, text=text,command=cn)
    actionNormal.grid(column=column1, row=row1)
    name = tk.StringVar()
    textNormal = ttk.Entry(order, width=30, textvariable=name)
    textNormal.grid(column=column2, row=row2)
    list=[]
    list.append(actionNormal)
    list.append(textNormal)
    print (list)
    #退出和清空按钮
    quitBt = ttk.Button(order, width=6, text='Quit',command=quitEvent)
    quitBt.grid(column=1, row=6)
    quitBt = ttk.Button(order, width=6, text='clear',command=clearEvent)
    quitBt.grid(column=2, row=6)
    return list

#------------------------------------------------------------------------

def quitEvent():
    ui.destroy()
def clearEvent():
    normal[1].delete(0,1000)
    vbkAOrder[1].delete(0,1000)
    vbkMOrder[1].delete(0, 1000)
    djOrder[1].delete(0, 1000)
#------------------------------------------------------------------------
#根据不同类型要求下单
normal=layOut("无需确认",1,2,1,1,clickNormal)
vbkAOrder=layOut("vbk自动",1,2,2,2,vbkAOrder)
vbkMOrder=layOut("vbk人工",1,2,3,3,vbkMOrder)
djOrder=layOut('云南大理',1,2,4,4,DJOrder)


orderLink()
ui.mainloop()
