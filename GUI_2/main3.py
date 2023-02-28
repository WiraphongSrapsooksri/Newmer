import numpy as np
from tkinter import * 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root =Tk()
root.title("Cat-Dog sale report")

x = np.array([2017,2018,2019,2020,2021,2020])
cat = np.array([200,210,230,200,240,180])
dog = np.array([150,200,250,180,250,200])

fig = plt.figure(figsize=(5,4))

plot1 = fig.add_subplot(111)
plot1.plot(x,cat,'r-' )
plot1.plot(x,dog,'g-')
plot1.legend()

plot1.set_xlabel('X')
plot1.set_ylabel('Y')


canvas = FigureCanvasTkAgg(fig,master=root)
canvas.get_tk_widget().place(x=0,y=0)

root.geometry('480x450')
root.mainloop()
