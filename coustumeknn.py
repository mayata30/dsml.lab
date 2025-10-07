import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
df=pd.read_csv("costume.csv")
x=df.iloc[:,:-1]
y=df.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Enter the data:")
a=float(input("Enter the height in cm:"))
b=float(input("Enter the weight in cm:"))
sample=[[a,b]]
pred=knn.predict(sample)
print("The class is:",pred[0])
