import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error,r2_score
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/polydata.csv")
x = df[['X']]
y = df['Y']




poly2_feature = PolynomialFeatures(degree=2)
x_poly2 = poly2_feature.fit_transform(x.values)
model_poly2 = LinearRegression()
model_poly2.fit(x_poly2,y.values)

b = model_poly2.coef_
a = model_poly2.intercept_
y_pred = model_poly2.predict(x_poly2)
r2 = r2_score(y,y_pred)
mse = mean_squared_error(y,y_pred)

print('slop (b): ',b)
print('Intercept (a): ',a)
print("R2\t : %.2f" %(r2))
print('MSE\t : %.2f'%(mse))

x_new = np.array([10,15,20]).reshape(-1,1)
y_pred = model_poly2.predict(poly2_feature.fit_transform(x_new))
print("Predict reponses for x_test\n",y_pred)

plt.scatter(x,y,color='green',label='Actual response')
# plt.scatter(x_new,y_pred,color='red',marker ='X',label = 'Predicted data')

x1 = np.linspace(10,20,100).reshape(-1,1)
y_pred = model_poly2.predict(poly2_feature.fit_transform(x1))
plt.plot(x1,y_pred,color='blue',label = 'Poly degree2: Y = %.2fX +%.2fX^2 + %.2f,(R2 = %.2f)'%(b[1],b[2],a,r2))


poly3_feature = PolynomialFeatures(degree=3)
x_poly3 = poly3_feature.fit_transform(x.values)
model_poly3 = LinearRegression()
model_poly3.fit(x_poly3,y.values)

b = model_poly3.coef_
a = model_poly3.intercept_
y_pred = model_poly3.predict(x_poly3)
r3 = r2_score(y,y_pred)
mse3 = mean_squared_error(y,y_pred)

print('slop (b): ',b)
print('Intercept (a): ',a)
print("R2\t : %.2f" %(r3))
print('MSE\t : %.2f'%(mse3))

x_new = np.array([10,15,20]).reshape(-1,1)
y_pred = model_poly3.predict(poly3_feature.fit_transform(x_new))
print("Predict reponses for x_test\n",y_pred)


x1 = np.linspace(10,20,100).reshape(-1,1)
y_pred = model_poly3.predict(poly3_feature.fit_transform(x1))
plt.plot(x1,y_pred,color='pink',label = 'Poly degree3: Y = %.2fX +%.2fX^2 + %.2fX^3 + %.2f,(R2 = %.2f)'%(b[1],b[2],b[3],a,r3))


modeLinear = LinearRegression()
modeLinear.fit(x.values,y.values)
bL =modeLinear.coef_
aL = modeLinear.intercept_
r_sq_Linear = modeLinear.score(x,y)
y_pred_Linear = modeLinear.predict(x)
r2_linear = r2_score(y,y_pred_Linear)
mse_Linear = mean_squared_error(y,y_pred_Linear)

x_new_Linear = np.array([10,15,20]).reshape(-1,1)
y_pred_Linear = modeLinear.predict(modeLinear_fe)

x1_Linear = np.linspace(10,20,100).reshape(-1,1)
x1_Linear = modeLinear.predict(x1_Linear)

plt.plot(x1_Linear,x1_Linear,color='aqua', label = ("Y = %.2fX + %.2f,(R2 = %.2f)"%(bL ,aL,r2_linear)))



plt.legend()
plt.show()