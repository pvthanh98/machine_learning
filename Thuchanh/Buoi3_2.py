from sklearn import datasets
import pandas as pd
import numpy as np
# iris = datasets.load_iris()
# # X = iris.data
# # Y = iris.target

data = pd.read_csv("nursery.data",header=None)
X =np.array(data.iloc[:,:8].values)
Y =np.array(data.iloc[:,8].values)

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3.0,random_state=0)
model = GaussianNB()
model.fit(X_train,Y_train)

thucte = Y_test
dubao = model.predict(X_test)

from sklearn.metrics import accuracy_score
print("Do chinh xac la ",accuracy_score(dubao,thucte)*100)
