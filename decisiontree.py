from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
DTC=DecisionTreeClassifier()
DTC.fit(x_train,y_train)
y_pred=DTC.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
print("enter the sample data")
a=int(input("enter sepal length in cm="))
b=int(input("enter sepal width in cm="))
c = int(input("enter petal length in cm="))
d = int(input("enter petal width in cm="))
sample=[[a,b,c,d]]
pred=DTC.predict(sample)
pred_v=[iris.target_names[p] for p in pred]
print(pred_v)
