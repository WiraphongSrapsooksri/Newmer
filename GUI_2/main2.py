import numpy as np
from tkinter import * 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Demo matplolib Graphs")

def clearEntry():
    filename_entry.delete(0,END)
    for widget in Canvas.winfo_children():
        widget.destroy()

ClearButton = Button(
    text="Clear",width=10,
    font= ('none 10'),
    bg = "slateGray1",
    fg = 'dark green',
    command= clearEntry
)

filename_entry = Entry(width=75 ,font= 'none 10')

x = np.random.randint(0,10,10)
y = np.random.randint(0,50,10)

fig = plt.figure(figsize=(8,8),dpi=100)

plot1 = fig.add_subplot(121)
plot1.plot(x,y,'ro' ,label='234')

plot1.set_title("HOW TO")
plot1.set_xlabel('X')
plot1.set_ylabel('Y')

plot2 = fig.add_subplot(122)
plot2.plot(x,y,'g-')

Canvas = FigureCanvasTkAgg(fig,master=root)
ClearButton.place(x=650,y=10)
Canvas.get_tk_widget().pack()

root.geometry('800x400')
root.mainloop()