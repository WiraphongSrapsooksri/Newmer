import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# generate root
root = ctk.CTk()
root.geometry("800x400")

# generate random numbers for the plot
x,y,s,c = np.random.rand(4,100)

# generate the figure and plot object which will be linked to the root element
fig, ax = plt.subplots()
fig.set_size_inches(8,4)
ax.scatter(x,y,s*50,c)
ax.axis("off")
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
canvas = FigureCanvasTkAgg(fig,master=root)
canvas.draw()
canvas.get_tk_widget().place(relx=0.15, rely=0.15)

# initiate the window
root.mainloop()