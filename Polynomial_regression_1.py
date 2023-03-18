import  numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error,r2_score
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

df = pd.read_csv("data/polydata.csv")
x = df[['X']]
y = df['Y']

poly2_feature = PolynomialFeatures(degree=2)
x_poly2 = poly2_feature.fit_transform(x.values)
model_poly2 =LinearRegression()
model_poly2.fit(x_poly2,y.values)

model_poly2_1 = LinearRegression()
model_poly2_1.fit(x,y)

b_1 = model_poly2_1.coef_
a_1 = model_poly2_1.intercept_
r_sq_1 = model_poly2_1.score(x,y)
y_pred_1  = model_poly2_1.predict(x)
r2_1 = r2_score(y,y_pred_1)
mse = mean_squared_error(y,y_pred_1)

print("b_1:",b_1)
print("a_1:",a_1)
print("r2",r2_1)

b = model_poly2.coef_
a = model_poly2.intercept_
y_pred = model_poly2.predict(x_poly2)
r2 = r2_score(y,y_pred)
mse = mean_squared_error(y,y_pred)

print("b:",b)
print("a:",a)
# print("y_pred",y_pred)
print("r2",r2)
print("mse",mse)

x_new = np.array([10,15,20]).reshape(-1,1)
y_pred = model_poly2.predict(poly2_feature.fit_transform(x_new))
print("Predict reponses for x_test\n",y_pred)

plt.scatter(x,y,color='green',label='Actual response')
plt.scatter(x_new,y_pred,color='red',marker='X',label='Predicted data')

x1 = np.linspace(10,20,100).reshape(-1,1)
y_pred = model_poly2.predict(poly2_feature.fit_transform(x1))
# plt.plot(x1,y_pred,color='blue',label='Polynomial: Y = %.2fX + %.2fX^2 + %.2f,(R2= %.2f)'% (b[1],b[2],a,r2))
plt.plot(x1,y_pred,color='blue',label='Polynomial: Y = %.2fX + %.2f,(R2= %.2f)'% (b_1,a_1,r2_1))

plt.legend()
plt.show()

