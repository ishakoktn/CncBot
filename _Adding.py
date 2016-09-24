# -*- coding: utf-8 -*-
#python3
#Coding by Ishak Okutan

import sqlite3,os,time
from pyautogui import _pyautogui_win as X

try:
    from Tkinter import Tk
except ImportError:
    from tkinter import Tk



Functions = ['Click()',
             'Compare()',
             'Write()'
                         ]

global vt,Db

def Create_Project(name):
    try:
        with sqlite3.connect(name + ".sqlite") as Db: 
            
            vt = Db.cursor()
            vt.execute("""CREATE TABLE Func_Order(name)""")
            vt.execute("""CREATE TABLE Capture_Data(pos,button)""")
            vt.execute("""CREATE TABLE Time(Value)""")
            Db.commit()
        return 1

    except:
        return 0

#Insert functions
    
def Compare(name,value,equal):
    """ Section of "equal": '>' , '<' ,'='
        You can compare your entered value to value of showed by cursor
        When you press 'ENTER' cursor must be on compare value"""
    with sqlite3.connect(name + ".sqlite") as Db: 
        vt = Db.cursor()
        cursorPos = X._position()
        vt.execute("""INSERT INTO Func_Order VALUES('Compare(),{},{}')""".format(str(value)
                                                                             ,equal))
        vt.execute("""INSERT INTO Capture_Data VALUES({})""".format((str(cursorPos[0])
                                                                   +","+
                                                                   str(cursorPos[1]))
                                                                                      ))
    #for compare we don't have to know click type of button. it's standart,position is enough                                                                             ))
        Db.commit()

def Write(name,text):
    """Go to text area with cursor and use this funcsion
       When you press 'ENTER' cursor must be on compare value"""
    with sqlite3.connect(name + ".sqlite") as Db: 
        vt = Db.cursor()
        cursorPos = X._position()
        vt.execute("""INSERT INTO Func_Order VALUES('Write(),{}')""".format(text))
        vt.execute("""INSERT INTO Capture_Data VALUES({})""".format(str(cursorPos[0])
                                                                   +","+
                                                                   str(cursorPos[1])
                                                                                    ))
                                                                                 
    #for write we don't have to know click type of button. it's standart,position is enough
        Db.commit()






def Click(name,button):
    """Sections: 'right' , 'left', 'middle' or 'Double Click' """
    with sqlite3.connect(name + ".sqlite") as Db: 
        vt = Db.cursor()
        cursorPos = X._position()
        vt.execute("""INSERT INTO Func_Order VALUES('Click(),{}')""".format(button))
        vt.execute("""INSERT INTO Capture_Data VALUES({})""".format(str(cursorPos[0])
                                                                   +","+
                                                                   str(cursorPos[1])
                                                                                      ))
        Db.commit()


def Time(name,value):
    """Enter like <hh.mm> (e.g. '01.25')"""
    with sqlite3.connect(name + ".sqlite") as Db: 
        vt = Db.cursor()                               
        vt.execute("""INSERT INTO Time VALUES({})""".format(value))
        Db.commit()


#Run functions

def _Compare(pixels,value,equal):
    Pix = Split(pixels)
    X._moveTo(int(Pix[0]),int(Pix[1]))
    X._click(int(Pix[0]),int(Pix[1]),'left')#Double Click
    X._click(int(Pix[0]),int(Pix[1]),'left')
    
    X._keyDown('ctrl')#Copy
    X._keyDown('c')
    X._keyUp('ctrl')
    X._keyUp('c')

    board = Tk()
    board.withdraw()
    Copyed_Txt = board.clipboard_get()#get text on clipboard
    
    
    if equal == '>':#find what happend after this function
        if value > Copyed_Txt:
            return 1    
        else:
            return 0

    elif equal == "=":
        if value == Copyed_Txt:
            return 1
        else:
            return 0

    elif equal == "<":
        if value < Copyed_Txt:
            return 1
        else:
            return 0

def _Click(pixels,button):
    Pix = Split(pixels)
    X._moveTo(int(Pix[0]),int(Pix[1]))
    
    if button[0] == 'D':#Double Click
        button = 'left'
        X._click(int(Pix[0]),int(Pix[1]),button)
    
    X._click(int(Pix[0]),int(Pix[1]),button)
    

def _Write(pixels,text):
    Pix = Split(pixels)
    
    os.system("echo {}|clip".format(text))#Copy text to clipboard
    X._moveTo(int(Pix[0]),int(Pix[1]))
    X._click(int(Pix[0]),int(Pix[1]),'left')

    X._keyDown('ctrl')#Paste
    X._keyDown('v')
    X._keyUp('ctrl')
    X._keyUp('v')
    


def Split(text):
    text = str(text)
    nwTxt =""
    lstTxt = list()
    for i in text[1:len(text)-1]:
        if i == ',':
            lstTxt.append(nwTxt)
            nwTxt = ""
        else:
            nwTxt += i
    lstTxt.append(nwTxt)
    return lstTxt
    
    
    




