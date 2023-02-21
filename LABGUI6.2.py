from tkinter import *
from tkinter.font import *
from PIL import Image,ImageTk


def Showimg(name):
    canvas.delete('all')
    if(name=='clear'):
        background.config(image='')
        background.config(width=72,height=25)
        return

    imgopae = Image.open('img/'+name+'.jpg')
    base_w = 550
    withbase = base_w/float(imgopae.size[0])
    heightbase = int(float(imgopae.size[1])*float(withbase))
    img= ImageTk.PhotoImage(imgopae.resize((base_w,heightbase),resample=3))
    canvas.create_image(0,0,anchor=NW,image=img)
    canvas.image = img
    canvas.pack()
    
root = Tk()
root.geometry('550x500')
root.title("Demo Positioning widgets")
LabelTitlte = Label(text='Show Image')
LabelTitlte.config(font='none 24',anchor=CENTER,width=30) 

btnCat = Button(text='at',width=15,command=lambda:Showimg('cat'))
btnDog = Button(text='Dog',width=15,command=lambda:Showimg('dog'))
btnPig = Button(text='Pig',width=15,command=lambda:Showimg('Pig'))
clear = Button(text='Clear',width=15,command=lambda:Showimg('Clear'))
lans = 130

LabelTitlte.pack()
btnCat.place(x=20+(lans*0),y=60)
btnDog.place(x=20+(lans*1),y=60)
btnPig.place(x=20+(lans*2),y=60)
clear.place(x=20+(lans*3),y=60)

background = Label(borderwidth=2,relief='groove',width=72,height=25)
background.place(x=20,y=100)
canvas= Canvas(background, width= 500, height= 350)
root.mainloop()