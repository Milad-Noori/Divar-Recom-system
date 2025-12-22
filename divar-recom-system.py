import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL.Image import preinit
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from tkinter import *
# def print_predict():
#
window = Tk()
window.title("House-price")
window.geometry("1300x700")
label = Label(window, text="House-price",background="gray",foreground="black",font=("Tahoma",20)).pack()
name_model = Label(window,text="Model name :",padx=10,pady=10)
name_model.place(x=50,y=100)

Address = Label(window,text="Address :",padx=10,pady=10)
Address.place(x=50,y=200)

Area = Label(window,text = "Area :",padx=15,pady=15)
Area.place(x=50,y=300)
area_entry=Entry(window)
area_entry.place(x=200,y=315,width=250,height=25)

Floor = Label(window,text = "Floor :",padx=15,pady=15)
Floor.place(x=50,y=400)
floor_entry=Entry(window)
floor_entry.place(x=200,y=412,width=250,height=25)

Room= Label(window,text = "Room :",padx=15,pady=15)
Room.place(x=50,y=500)
room_entry=Entry(window)
room_entry.place(x=200,y=512,width=250,height=25)

Parking = Label(window,text = "Parking :",padx=15,pady=15)
Parking.place(x=700,y=100)



YearOfConstruction = Label(window,text="YearOfConstruction :",padx=10,pady=10)
YearOfConstruction.place(x=700,y=200)

Warehouse = Label(window,text="Warehouse :",padx=10,pady=10)
Warehouse.place(x=700,y=300)

price= Label(window,text = "🏷️Price :",padx=15,pady=15)
price.place(x=400,y=600)

Button = Button(window,text = "textPredict",padx=20,pady=10,bd=10)
Button.place(x=50,y=600)
window.mainloop()


# df.shape()
# df.head()
# df.describe()
# df.isnull().sum()
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