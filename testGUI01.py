from tkinter import *
from tkinter.font import *

root = Tk()

l1 = Label(text='Hi, I\'m a simple Label')
Hel20 = Font(family="Helvetica",size=20,weight='bold')
l2 = Label(text='Hi ,I/m another Lable')
l2.config(font=Hel20,fg='plum3')

l3= Label(
    text    ='I/m a huge gray Lable',
    width   =50,
    height  =10,
    fg      ='green',
    bg      ='lightgray',
    font    ='Helvetica 30 bold'
)
btn = Button(text='Test Btn')
btn.config(font=Hel20,fg='plum3')



l1.pack()
l2.pack()
l3.pack()
for i in range(0,10):
    btn = Button(text='Test Btn')
    btn.config(font=Hel20,fg='plum3')
    btn.pack() 
root.mainloop()