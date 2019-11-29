import numpy as np
import pandas as pd # Read csv


from sklearn.tree import DecisionTreeClassifier # Decision Tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split # Split training and testing data
from sklearn.naive_bayes import GaussianNB

#tien xu ly du lieu
from sklearn.preprocessing import LabelEncoder # Transform 'string' into class number
def xuLyDuLieu(file):
    #Doc file
    data = pd.read_csv(file)
    encoder = {}
    #Nhan du lieu
    labels = ['parents','has_nurs','form','children','housing','finance','social','health','application']
    for label in labels:
        #Ma hoa nhan
        lbEncode = LabelEncoder()
        lbEncode.fit(data[label])
        encoder[label] = lbEncode
        #Chuyen du lieu sang gia tri so
        data[label] = lbEncode.transform(data[label])
    return data, encoder

if __name__ == '__main__':
    data, label = xuLyDuLieu('nursery.csv')
    #Lay du lieu 
    X = data.iloc[:,0:8].values
    Y = data.iloc[:,8].values
    
    #Phan chia du lieu 1/3 cho test va 2/3 cho traing 
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42, test_size=0.3)
    
    #Trainning Bayes GaussianNB
    gnb = GaussianNB()
    gnb.fit(X_train,Y_train)
    
    #Tien hanh du doan cho tap x_test
    Y_pred = gnb.predict(X_test)
    
    #Tinh do chinh xac
    from sklearn.metrics import confusion_matrix
    cnf_matrix = confusion_matrix(Y_test, Y_pred)
    print("Ma tran cua GaussianNB:")
    print(cnf_matrix)
    print("Do chinh xac GaussianNB: ", accuracy_score(Y_test,Y_pred)*100)
    
    #Training su dung mo hinh DecisionTreeClassifer theo chi so entropy
    clf = DecisionTreeClassifier(criterion="entropy",random_state=42, min_samples_leaf=5)
    clf.fit(X_train, Y_train)
    Y_pred = clf.predict(X_test)
    cnf_matrix = confusion_matrix(Y_test, Y_pred)
    print('\n')
    print("==================================================")
    print("Ma tran cua DecisionTree:")
    print(cnf_matrix)
    print('Do chinh xac DecisionTree: ', accuracy_score(Y_test,Y_pred)*100)
    
    # print(lbEncode.inverse_transform([0,1,2,3,4]))

  