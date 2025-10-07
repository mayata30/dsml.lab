import numpy as np
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

iris=np.read_csv('iris.csv')

x=iris.iloc[:,:3]
y=iris.iloc[:,2]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

lr=LinearRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(y_train)

print("Mean absolute error: ",metrics.mean_absolute_error(y_test,y_pred))
print("Mean squared error: ",metrics.mean_squared_error(y_test,y_pred))
print("R squared score: ",metrics.r2_score(y_test,y_pred))

print("Enter the values: ")
a=float(input("Enter the sepal length in CM: "))
b=float(input("Enter the sepal width in CM: "))
c=float(input("Enter the petal width in CM: "))
sample=[[a,b,c]]
pred=lr.predict(sample)
print("The predicted value for petal length is: ",pred[0])
