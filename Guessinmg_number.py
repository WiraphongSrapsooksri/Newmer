from tkinter import *
from tkinter.font import *
import numpy as np

minNumber = 0
maxNumber = 20
correctNumber = np.random.randint(minNumber,maxNumber)
count = 0
def checkNumber(event):
    global minNumber,maxNumber,correctNumber,count
    textAns = ''
    temp = int(inputtext.get())
    if(temp == correctNumber):
        textAns = 'ถูกแล้ว '+str(count)+' ครั้ง'
    elif(correctNumber>temp):
        textAns = 'น้อยไป ตอบใหม่'
        minNumber = temp +1
    elif(correctNumber<temp):
        textAns = 'มากไป ตอบใหม่'
        maxNumber = temp-1
    else:
        textAns = 'Error'

    outputLabel.config(text=textAns)
    minLabel.config(text=minNumber)
    maxLabel.config(text=maxNumber)
    count = count +1

root = Tk()
root.geometry("500x380")
minLabel = Label(text=minNumber,width=10,height=5,borderwidth=2,relief='groove',font='ChakraPetch-Bold 30')
maxLabel = Label(text=maxNumber,width=10,height=5,borderwidth=2,relief='groove',font='ChakraPetch-Bold 30')
inputtext = Entry(width=22,borderwidth=2,relief='groove',font='ChakraPetch-Bold 30',justify=CENTER)
outputLabel =  Label(text='เดาตัวเลข',width=21,borderwidth=2,relief='groove',font='ChakraPetch-Bold 30')
inputtext.bind('<Return>',checkNumber)

inputtext.place(x=5,y=5)
minLabel.place(x=5,y=60)
maxLabel.place(x=258,y=60)
outputLabel.place(x=5,y=300)
root.mainloop()