import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report , accuracy_score , confusion_matrix
import pandas as pd

df = pd.read_csv("data/interview.csv")

x = df[['english','gpa','experience']]
y = df['admitted']  ## ค่าความจริง ว่าเป็นไง รับ หรือ ไม่รับ

model = LogisticRegression(random_state=0)
model.fit(x.values,y.values)

print("Model.classes_ ",model.classes_)  ## Model.classes_  ['Accepted' 'Rejected']
print("Intercept: ",model.intercept_)  ##Intercept:  [25.06899467]
print("Coef     : ",model.coef_)   ## Coef     :  [[-0.04889993 -1.49562539 -0.85820154]]
print("R2:      : ",model.score(x.values,y.values))  ## R2:      :  0.9655172413793104   แม่นยำมาก ค่าสูง

proba = model.predict_proba(x.values)
y_pred = model.predict(x.values)
print("___SOME Predicter Values and y_pred____") #loop show data result
for i in range(y.shape[0]):
    print('{}\t{}\t{}'.format(proba[i],y[i],y_pred[i]))
    #[0.02185919 0.97814081]	Rejected	Rejected
                                                            # proba[i] [0.02185919 0.97814081]  ['english','gpa','experience']
                                                            # y[i] ความจริงนั้นๆ  Rejected
                                                            # y_pred[i] สั่งที่คาดการณ์ Rejected
    #[0.6855586 0.3144414]	Accepted	Accepted

cm = confusion_matrix(y.values,y_pred)
print("\n____Confusion Matrix____\n",cm)

print("Accuracy: %.2f"%(accuracy_score(y,y_pred)))

print("____Classification_report____")
print(classification_report(y.values,model.predict(x.values)))

#Predict some valies of x
x_new = np.array([[500,3.25,0],[300,2.25,4],[300,2.25,10]])
y_pred = model.predict(x_new)
print("printdict response:",y_pred,sep='\n')