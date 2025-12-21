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
window.geometry("1300x500")
label = Label(window, text="House-price",background="gray",foreground="black",font=("Tahoma",20)).pack()
name_model = Label(window,text="Model name :",padx=10,pady=10)
name_model.place(x=50,y=100)
Address = Label(window,text="Address :",padx=10,pady=10)
Address.place(x=50,y=150)
Area = Label(window,text = "Area :",padx=15,pady=15)
Area.place(x=50,y=200)
Floor = Label(window,text = "Floor :",padx=15,pady=15)
Floor.place(x=50,y=250)
Parking = Label(window,text = "Parking :",padx=15,pady=15)
Parking.place(x=50,y=300)






Button = Button(window,text = "Predict",padx=15,pady=15)
Button.place(x=600,y=400)
window.mainloop()


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