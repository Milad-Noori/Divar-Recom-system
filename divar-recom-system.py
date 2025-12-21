import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from tkinter import *
window = Tk()
window.title("House-price")
window.minsize(500,500)
window.maxsize(700,700)
# df.shape()
# df.head()
# df.describe()
# df.innull().sum()
# data = pd.read_csv("HouseNew.csv")
# df1 = pd.DataFrame(data)
# df1.isnull().sum()
# print(df1)
# # X=pd.DataFrame(df1,columns=['Elevator','Floor','Parking','Room',
# #                             'Warehouse','YearOfConstruction',
# #                             'Address'])
# Y=df1['Price'].values.reshape(-1,1)
# X_train,X_test , Y_train,Y_test = train_test_split(X,Y ,test_size = 0.2, random_state = 0)
# lr=LinearRegression()
# lr.fit(Y_test,Y_train)
# y_pred =lr.predict(X_test)
# print("mae",metrics.mean_absolute_error(Y_test,y_pred))
# print("mae",mean_absolute_error(Y_test,y_pred))
# print(np.sqrt(metrics.mean_absolute_error(Y_test,y_pred)))
# print(y_pred)



window.mainloop()