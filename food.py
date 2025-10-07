import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
df = pd.read_csv("food.csv")
print(df.columns) 
x = df[['sweetness', 'crunchyness']] 
y = df['foodtype']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
knn = KNeighborsClassifier(n_neighbors=2 )
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Enter the data:")
a = float(input("Enter the sweetness : "))
b = float(input("Enter the crunchyness: "))
sample = pd.DataFrame([[a, b]], columns=['sweetness', 'crunchyness'])  
pred = knn.predict(sample)
print("The class is:", pred[0])
