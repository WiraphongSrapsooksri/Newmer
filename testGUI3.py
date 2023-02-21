from tkinter import *
from tkinter.font import *

def nameCallback():
    name = nameEntry.get()
    nameLabel.config(text="welcome "+name)
def clearEntry():
    nameEntry.delete(0,'end')
    nameLabel.config(text='')

root = Tk()
root.geometry("340x100")
nameEntry = Entry(width=30)
nameButton = Button(text='Click Me',command=nameCallback)
clearButton = Button(text='Clear Me')
nameLabel = Label(fg='green',width=20,borderwidth=2,relief='groove',font='none 20')
clearButton.config(command=clearEntry)

nameEntry.place(x=5,y=5)
nameButton.place(x=200,y=5)
clearButton.place(x=270,y=5)
nameLabel.place(x=5,y=40)

root.mainloop()