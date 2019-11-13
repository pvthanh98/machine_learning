import numpy as np
import pandas as pd

data = pd.read_csv("advertising.csv")
X = data.iloc[:,1:4].values
Y = data["Sales"].values

import sklearn 
from sklearn import linear_model
lm = linear_model.LinearRegression()

lm.fit(X[0:180],Y[0:180])
print(lm.intercept_)
print(lm.coef_)

y_test = Y[-20:]
x_test = X[-20:]
y_pred = lm.predict(x_test)


import matplotlib.pyplot as plt
plt.plot(y_pred,color="red")
plt.plot(y_test, color="green")
plt.show()