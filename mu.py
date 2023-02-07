import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd

#Multiple Lenear Regression Lab
df = pd.read_csv("data/quiz7.csv")

y = df['price']
x = df[['weight', 'age']]

model = LinearRegression()
model.fit(x.values, y.values)

b = model.coef_
a = model.intercept_
y_pred = model.predict(x.values)
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)
print("All bi: ", b)
print("a:   ", a)
print("R2: ",r2)
print("Linear eqauation:\t Y = %.2FWeight + %.2fAge + %.2f"
    %(b[0], b[1], a))

print("R_squared\t : %.2f" %(r2))
print("MSE\t : %.2f" %(mse))

x_new = ([[120, 40]])
y_pred_new = model.predict(x_new)
np.set_printoptions(precision=2)
print("\nPredicted response of X: ", y_pred_new)

#Simple Linear Regression Quiz7
df = pd.read_csv("data/quiz7.csv")

print('---------------------------------\nSimple Linear Regression')
x_column = ['weight', 'age']
y = df['price']
weight_age = [120, 40]

for i in range(len(x_column)):
    x = df[[x_column[i]]]

    model = LinearRegression()
    model.fit(x.values,y.values)

    b = model.coef_
    a = model.intercept_
    r_sq = model.score(x,y)
    y_pred = model.predict(x)
    r2 = r2_score(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    

    x1 = np.linspace(np.min(x), np.max(x), 2).reshape(-1,1)
    y1 = model.predict(x1)

    x_new = ([[weight_age[i]]])
    y_pred_new = model.predict(x_new)
    np.set_printoptions(precision=2)
    
    print("MSE " + x_column[i] + " = %.2f" %mse)
    print("\nPredicted response of X (" + x_column[i] + "): ", y_pred_new)
    # print("a: %.2f  "%(a))
    # print("R2: %.2f"%(r2))
    # print("Linear eqauation:\t Y = %.2FWeight + %.2fAge + %.2f"%(b[0], b[1], a))
    # print("R_squared\t : %.2f" %(r2))

    plt.subplot(2,1,i+1)
    plt.scatter(x,y, color='green')
    plt.plot(x1,y1, 'blue', label = ("Y = %.2fX + %.2f, (R2 = %.2f)" %(b,a,r2)))
    plt.legend()
    plt.xlabel(x_column[i])
    plt.ylabel("price")

plt.show()





