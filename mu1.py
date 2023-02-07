import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("data/quiz7.csv")

print('---------------------------------\nSimple Linear Regression')
xd = ['weight', 'age']
y = df['price']
dc = ['pink', 'yellow']
lc = ['magenta', 'green']

for i in range(len(xd)):
    x = df[[xd[i]]] #15

    model = LinearRegression()   #16
    model.fit(x.values,y.values)  #17

    b = model.coef_
    a = model.intercept_
    r_sq = model.score(x.values,y.values)
    y_pred = model.predict(x.values)
    r2 = r2_score(y, y_pred)  #18
    mse = mean_squared_error(y, y_pred)
    print("MSE : " + xd[i] + " = %.2f" %mse)

    x1 = np.linspace(np.min(x), np.max(x), 2).reshape(-1,1)
    y1 = model.predict(x1)
 
    plt.scatter(x,y, color=dc[i], label=xd[i])  #19
    plt.plot(x1,y1, lc[i], label = ("Y = %.2fX + %.2f, (R2 = %.2f)" %(b,a,r2)))  #20

    plt.legend()
    plt.xlabel("Weight or Age")
    plt.ylabel("price")

plt.show()