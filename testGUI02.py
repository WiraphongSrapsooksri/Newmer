from tkinter import *
from tkinter.font import *
from numpy import random as rn

def nameCallback():
    name = e1.get()
    l5.config(text="Welcoe "+name)
def clearEntry():
    e1.delete(0,'end')
    l5.config(text='')
def randomColor():
    r = rn.randint(0,255)
    g = rn.randint(0,255)
    b = rn.randint(0,255)
    return f'#{r:02x}{g:02x}{b:02x}'

def changeColor():
    l5.config(bg =randomColor(),fg=randomColor())
root = Tk()
root.geometry('520x250')
root.title("Demo Positioning widgets")
l1 = Label(borderwidth=2,relief='raised',text='raised,PositionL(5,10)')
l2 = Label(borderwidth=2,relief='ridge',text='ridge,PositionL(5,10)')
l3 = Label(borderwidth=2,relief='groove',text='groove,PositionL(5,10)')
l4 = Label(borderwidth=2,relief='solid',text='solid,PositionL(5,10)')
l5 = Label(fg='green',width=20,borderwidth=2,relief='groove',font='none 20')

b1 = Button(text='Click',width=40,anchor=CENTER,command=nameCallback)
b2 = Button(text='Random',width=40,anchor=CENTER,command=changeColor)
b3 = Button(text='Clear',width=40,anchor=CENTER)
e1 = Entry()
# e2 = Entry(bg='LightBlue1',fg='Green4',font='none 15',width=45)


b3.config(command=clearEntry)

l1.place(x=5,y=10)
l2.place(x=5,y=40)
l3.place(x=5,y=100)
l4.place(x=5,y=150)
l5.place(x=5,y=200)

b1.place(x=200,y=10)
b2.place(x=200,y=50)
b3.place(x=200,y=100)
e1.place(x=200,y=150)
# e2.place(x=5,y=200)

root.mainloop()