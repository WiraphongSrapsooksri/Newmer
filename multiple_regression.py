import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/quiz7.csv")

y = df['price']
x = df[['weight'],['age']]

model = LinearRegression()
model.fit(x.values, y.values)

b = model.coef_
a = model.intercept_
y_pred = model.predict(x.values)
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)

print("All bi: ", b)
print("a:   ", a)
print("Linear eqauation:\t Y = %.2FWeight + %.2fAge + %.2f"%(b[0], b[1], a))
print("R_squared\t : %.2f" %(r2))
print("MSE\t : %.2f" %(mse))
