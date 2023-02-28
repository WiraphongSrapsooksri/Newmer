from tkinter import *
import matplotlib.pyplot as plt
from tkinter import messagebox
import numpy as np
from tkinter import * 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from pandastable import Table
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


df = pd.read_csv('../data/salary.csv')
x = df[['experience']]
y = df['salary']


model = LinearRegression()
model.fit(x,y)
b  =model.coef_
a = model.intercept_
r_sq = model.score(x,y)
y_pred = model.predict(x)
r2 = r2_score(y,y_pred)
mse = mean_squared_error(y,y_pred)
print(y)

def show_data():
    plot.plot(x,y,'go',Label='data')
    plot.legend()
    canvas.draw()

def show_regression():
    plt.plot(x,y, 'blue', label = ("Y = %.2fX + %.2f, (R2 = %.2f)" %(b,a,r2)))
    plot.legend()
    canvas.draw()
    dataButton['state']  = 'disble'

def predict_data():
    global y_pred
    print("Predict",y_pred)
    p = (int)(inputEntry.get())
    # print(p)
    y_pred = (int)(model.predict([[p]]))
    print(y_pred)
    messagebox.showinfo(title=f'Salay Prediction',message = f'experience:{p}\nSalary={y_pred}')


root = Tk()
root.title("Salary reeport")

fig = plt.figure(figsize=(5,4))
plot = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig,master=root)

dataButton = Button(text = 'Show Data', width=10,font = ('none 10'),command=show_data)
regressionButton = Button(text = 'Regression', width=10,font = ('none 10'),command=show_regression)
predictbutton = Button(text = 'Predict', width=10,font = ('none 10'),command=predict_data)
inputEntry = Entry(width = 12 ,font = ('none 10'))

dataButton.place (x=150,y=40)
regressionButton.place(x=250,y=40)
predictbutton.place(x=350,y=40)
inputEntry.place(x=350,y=10)

root.geometry('600x550')
root.mainloop()
