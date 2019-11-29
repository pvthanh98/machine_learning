import numpy as np
import pandas as pd # Read csv

from sklearn.naive_bayes import GaussianNB # Gaussian Naive Bayes
from sklearn.preprocessing import LabelEncoder # Transform 'string' into class number
# Because the fit function of GaussianNB only accept numeric input
from sklearn.model_selection import train_test_split # Split training and testing data
from sklearn import metrics # Evaluate model

def loadData(path):
    inputData = pd.read_csv(path)

    # Transform 'string' into class number
    Labels = [
        ['usual', 'pretentious', 'great_pret'],
        ['proper', 'less_proper', 'improper', 'critical', 'very_crit'],
        ['complete', 'completed', 'incomplete', 'foster'],
        ['1', '2', '3', 'more'],
        ['convenient', 'less_conv', 'critical'],
        ['convenient', 'inconv'],
        ['nonprob', 'slightly_prob', 'problematic'],
        ['recommended', 'priority', 'not_recom'],
        ['not_recom', 'recommend', 'very_recom', 'priority', 'spec_prior']
    ]

    le = LabelEncoder()

    # Somehow use np.mat to deal with shape problem down below
    dataTemp = np.mat(np.zeros((len(inputData), len(inputData.columns))))
    for colIdx in range(len(inputData.columns)):
        le.fit(Labels[colIdx])
        dataTemp[:, colIdx] = np.mat(le.transform(inputData.iloc[:, colIdx])).T

    num_data = np.array(dataTemp[:, :-1])
    num_label = np.array(dataTemp[:, -1])
    data_train, data_test, label_train, label_test = train_test_split(num_data, num_label, test_size=0.3, random_state=87)
    return data_train, label_train, data_test, label_test
    

data_train, label_train, data_test, label_test = loadData('nursery.csv')

    
print(data_test)
print(data_train)