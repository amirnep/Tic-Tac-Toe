from tkinter import *
from tkinter.colorchooser import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.title('Tic-Tac-Toe')
win.geometry('240x213')
win.resizable(False,False)

top2 = Toplevel(win)
top2.geometry('200x150')
top2.resizable(False,False)
top2.title('Welcome')
lb3 = Label(top2,text = 'Welcome to Tic-tac-toe')
lb3.config(font = ('mitra',10,'bold'))
lb3.pack()
lb4 = Label(top2,text = '''Player1 is X and Player2 is O
You can use help to know about
how to play and about producer, 
Let's Start the game.
''')
lb4.config(font = ('mitra',10))
lb4.pack()
btn10 = ttk.Button(top2,text = 'Start',width = 7,command = top2.destroy)
btn10.pack()

menubar = Menu(win)
win.config(menu = menubar)
filemenu = Menu(menubar, tearoff = 0)

def top():
    top = Toplevel(win)
    top.geometry('220x180')
    top.resizable(False,False)
    top.title('Help')
    lb = Label(top,text = 'Tic-tac-toe, noughts and crosses')
    lb.config(font = ('mitra',10,'bold'))
    lb.pack(side = 'top')
    lb1 = Label(top,text = '''is a paper and pencil game for two
players, X and O, who take turns   
marking the spaces in a 3x3 grid.  
The player who succeeds in placing
three of their marks in a horizontal  
, vertical, or diagonal row is the   
winner.''')
    lb1.config(font = ('mitra',10))
    lb1.pack()
    btn = ttk.Button(top,text = 'Exit',width = 5,command = top.destroy)
    btn.pack()

def top1():
    top1 = Toplevel(win)
    top1.geometry('210x270')
    top1.resizable(False,False)
    top1.title('About')
    lb2 = Label(top1,text = '''This game is provided by Amir  
Nemat pour, with python for
University project.
Tic-tac-toe is a nostalgiac game
for kids and now they can play on
windows.

About producer:
I'm Amir Nemat pour 19 Years old
From Iran,Tabriz.
I'm a Computer Engineer
student Term 2 from Shahid
Madani Azarabaijan University.
''')
    lb2.config(font = ('mitra',10))
    lb2.pack()
    btn0 = ttk.Button(top1,text = 'Exit',width = 5,command = top1.destroy)
    btn0.pack()

helpmenu = Menu(menubar, tearoff = 0)
help1 = Menu(helpmenu, tearoff = 0)
helpmenu.add_command(label = 'Help', command = top)
menubar.add_cascade(label = 'Help', menu = helpmenu)
helpmenu.add_command(label = 'About', command = top1)

exitmenu = Menu(menubar, tearoff = 0)
exitmenu.add_command(label = 'Exit', command = win.destroy)
menubar.add_cascade(label = 'Exit', menu = exitmenu)

click = True
def checker(buttons):
    global click
    if buttons["text"] == '' and click == True:
        buttons["text"] = "X"
        click = False
    elif buttons["text"] == '' and click == False:
        buttons["text"] = "O"
        click = True
    elif(btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X" or
         btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X" or
         btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X" or
         btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X" or
         btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X" or
         btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X" or
         btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X" or
         btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X"):
        messagebox.showinfo('Winner X','Player1 is Win the game')

    elif(btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O" or
         btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O" or
         btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O" or
         btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O" or
         btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O" or
         btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O" or
         btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O" or
         btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O"):
        messagebox.showinfo('Winner O','Player2 is Win the game')
    else:
        messagebox.showinfo('Draw','Round Draw.')

buttons = StringVar()
btn1 = Button(win,text = '',font = ('Times 10 bold'),height = 4,width = 10, command = lambda:checker(btn1))
btn1.grid(row = 0, column = 1)
btn2 = Button(win,text = '',font = ('Times 10 bold'),height = 4,width = 10, command = lambda:checker(btn2))
btn2.grid(row = 0, column = 2)
btn3 = Button(win,text = '',font = ('Times 10 bold'),height = 4,width = 10, command = lambda:checker(btn3))
btn3.grid(row = 0, column = 3)
btn4 = Button(win,text = '',font = ('Times 10 bold'),height = 4,width = 10, command = lambda:checker(btn4))
btn4.grid(row = 1, column = 1)
btn5 = Button(win,text = '',font = ('Times 10 bold'),height = 4,width = 10, command = lambda:checker(btn5))
btn5.grid(row = 1, column = 2)
btn6 = Button(win,text = '',font = ('Times 10 bold'),height = 4,width = 10, command = lambda:checker(btn6))
btn6.grid(row = 1, column = 3)
btn7 = Button(win,text = '',font = ('Times 10 bold'),height = 4,width = 10, command = lambda:checker(btn7))
btn7.grid(row = 2, column = 1)
btn8 = Button(win,text = '',font = ('Times 10 bold'),height = 4,width = 10, command = lambda:checker(btn8))
btn8.grid(row = 2, column = 2)
btn9 = Button(win,text = '',font = ('Times 10 bold'),height = 4,width = 10, command = lambda:checker(btn9))
btn9.grid(row = 2, column = 3)

mainloop()
