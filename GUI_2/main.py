import pandas as pd
from tkinter import * 
from tkinter import filedialog
from tkinter import messagebox as msg
from pandastable import Table

root = Tk()
root.title("Read Csv file")


def readCSV():
    try: 
        file_name = filedialog.askopenfilename(
            initialdir='.',
            title='Select Csv/ecvel file',
            filetypes=(('csv file','*.csv'),)
        )
        df = pd.read_csv(file_name)
        if(len(df)!=0):
            filename_entry.delete(0,END)
            filename_entry.insert(0,file_name)
            table = Table(frame,dataframe=df,read_only=True, width = 720,height = 500)
            table.show()
        else:
            msg.showinfo("No data records!",'Mo records')
    except FileNotFoundError as error:
        filename_entry.delete(0,END)

def clearEntry():
    filename_entry.delete(0,END)
    for widget in frame.winfo_children():
        widget.destroy()

filename_entry = Entry(width=75 ,font= 'none 10')

browseButton = Button(
    text= 'Browse',width=10,
    font= ('none 10'),
    bg = 'SlateGray1',
    command= readCSV
)
ClearButton = Button(
    text="Clear",width=10,
    font= ('none 10'),
    bg = "slateGray1",
    fg = 'dark green',
    command= clearEntry
)
exit_button = Button(
    text='Exit',width=6,
    font=('none 10'),
    bg = 'azure',
    fg =  'red',
    command= root.deiconify
)
frame = Frame()

filename_entry.place(x=10,y=10)
browseButton.place(x=550,y=10)
ClearButton.place(x=650,y=10)
exit_button.place(x=750,y=10)
frame.place(x=10,y=60)

root.geometry('820x600')
root.mainloop()