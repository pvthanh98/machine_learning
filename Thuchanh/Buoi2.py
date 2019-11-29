from sklearn.datasets import load_iris
iris_dt = load_iris()
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(iris_dt.data,iris_dt.target,test_size=1/3.0,random_state=5)
from sklearn.tree import DecisionTreeClassifier
clf_gini = DecisionTreeClassifier(criterion="gini",random_state=100,max_depth=3,min_samples_leaf=5)
clf_gini.fit(X_train,Y_train)
Y_pred = clf_gini.predict(X_test)

from sklearn.metrics import accuracy_score
print("Do chinh xac la ",accuracy_score(Y_pred,Y_test)*100)


import matplotlib.pyplot as plt;
plt.plot(X_test,Y_pred,"go",color="red")

plt.plot(X_test,Y_test,"go",color="green")
plt.xlabel("X")
plt.show()
#Doc du lieu bang pandas
# import pandas as pd
# import numpy as np
# data = pd.read_csv("iris.data", header=None)
# X = data.iloc[:,:4].values
# Y = np.array(data.iloc[:,-1:])

# from sklearn.model_selection import train_test_split
# X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3.0,random_state=5)

# from sklearn.tree import DecisionTreeClassifier
# clf_gini = DecisionTreeClassifier(criterion="gini",random_state=100,max_depth=3,min_samples_leaf=5)
# clf_gini.fit(X_train,Y_train)
# Y_pred = clf_gini.predict(X_test)

# from sklearn.metrics import accuracy_score
# print("Do chinh xac la ",accuracy_score(Y_pred,Y_test)*100)

