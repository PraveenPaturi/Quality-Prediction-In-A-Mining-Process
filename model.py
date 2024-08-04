import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

#Importing the Dataset
df=pd.read_csv('MiningProcess_Flotation_Plant_Database.csv', decimal=',',parse_dates=["date"],infer_datetime_format=True, sep=',')

df=df.set_index('date')
df = df.reset_index()
df=df.groupby(df.index//30).median()
 
df=df.drop(['Flotation Column 04 Air Flow', 'Ore Pulp Flow', 'Flotation Column 05 Air Flow', 'Flotation Column 03 Level', 'Flotation Column 01 Level', 'Flotation Column 02 Level', 'Ore Pulp Density', 'Flotation Column 06 Air Flow', 'Flotation Column 07 Air Flow', '% Silica Feed', 'Starch Flow', '% Iron Feed', 'Flotation Column 06 Level', 'Ore Pulp pH'], axis=1)

Y1 = df['% Silica Concentrate']
X1= df.drop(['% Silica Concentrate'], axis=1)

#Splitting Training and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X1, Y1,test_size = 0.2, random_state=30)

X = X_train.iloc[:,:].values
y = y_train.iloc[:].values

#Instantiate Multiple linear regression model
from sklearn import linear_model as lm
regressor=lm.LinearRegression()
regressor.fit(X,y) 

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[556.9075, 250.3695, 249.472 , 250.472 , 405.9865, 408.896 , 406.447 ,  66.07  ]]))



 
