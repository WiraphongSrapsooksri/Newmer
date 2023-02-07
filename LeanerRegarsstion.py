import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd
#Simple Linear Regression 7/2/2566
# df = pd.read_csv("data/walk.csv")


# y = df['distance']
# x = df[['time', 'temperature', 'age' ,'weight']]

# model = LinearRegression()
# model.fit(x.values,y.values)

# b = model.coef_
# a = model.intercept_
# y_pred = model.predict(x)
# r2 = r2_score(y,y_pred)
# mse = mean_squared_error(y,y_pred)
# print("a:   ",a)
# print("Linear qeqauation:/t Y = %.2f  TIME + %.2f  TEMP + %.2f Age + %.2f  Weight + %.2f"%(b[0],b[1],b[2],b[3],a))

# # x1 = ([[200,30,25,53],[150,30,20,65],[20,25,30,55],[50,20,22,85]])

# x1 = ([[200,30,25,53]])
# y1 = model.predict(x1)
# np.set_printoptions(precision=2)
# print("\nPredicted response of X:",y1)


# plt.scatter(x,y, color='green')
# plt.plot(x1,y1, 'blue', label = ("Y = %.2fX + %.2f, (R2 = %.2f)" %(b,a,r2)))
# plt.legend()
# plt.xlabel(x)
# plt.ylabel("distance")
# plt.show()

# print("=============SHOW===========")

df = pd.read_csv("data/quiz7.csv")
x_column = ['price', 'weight', 'age']
y = df['distance']

for i in range(len(x_column)): ## หาค่าของแต่ละรอบออกมาแล้วนำมา loop 4 ครั้ง เพื่อแสดง 4 กราฟ
    x = df[[x_column[i]]]

    model = LinearRegression()
    model.fit(x.values,y.values)

    b = model.coef_
    a = model.intercept_
    r_sq = model.score(x,y)
    y_pred = model.predict(x)
    r2 = r2_score(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    print("Linear qeqauation:/t Y = %.2f  TIME + %.2f  TEMP + %.2f Age + %.2f  Weight + %.2f"%(b[0],b[1],b[2],b[3],a))

    x1 = np.linspace([[200,30,25,53],[150,30,20,65],[20,25,30,55],[50,20,22,85]], 2).reshape(-1,1)
      # x1 = np.linspace(np.min(x), np.max(x), 2).reshape(-1,1)
    # x1 = ([[200,30,25,53],[150,30,20,65],[20,25,30,55],[50,20,22,85]])
    y1 = model.predict(x1)

    plt.subplot(2,2,i+1)

    plt.scatter(x,y, color='green')
    plt.plot(x1,y1, 'blue', label = ("Y = %.2fX + %.2f, (R2 = %.2f)" %(b,a,r2)))
    plt.legend()
    plt.xlabel(x_column[i])
    plt.ylabel("distance")

plt.show()