import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from streamlit import metric
import numpy as np

df = pd.read_csv("HouseNew.csv")


df['Elevator'] = df['Elevator'].astype('int')
df['Parking'] = df['Parking'].astype('int')
df['Warehouse'] = df['Warehouse'].astype('int')
# df['Elevator'] = df['Elevator'].map({True:1,False:0})
# Age
df["Age"] = 1404 - df["YearOfConstruction"]
# print(df[["YearOfConstruction","Price","Age"]].head(10).to_string())
# HasElevatorParking
# print(df.dtypes)

# print(address_counts)
df["Address"] = df["Address"].fillna("نامشخص")
address_counts = df["Address"].value_counts()

# print(df['Address'].nunique())
# print(df.head(10).to_string())
from sklearn.preprocessing import LabelEncoder, StandardScaler,MinMaxScaler
le = LabelEncoder()
df['Address_Encoded'] = le.fit_transform(df['Address'])

# df = df.drop('Address', axis=1)
# print(df.columns)
# print(df.head(10).to_string())



# print(df.columns)
# X = df.drop('Price',axis=1) # Features

# print(df.isna().sum())
print(df['Floor'].value_counts())
df['Floor'] = df['Floor'].fillna(df['Floor'].mode()[0]).astype('int')
print(df['Floor'].value_counts())

# sns.heatmap(df[['Elevator','Floor','Area','Parking','Room','Warehouse','YearOfConstruction','Address_Encoded','Price']].corr())
# plt.show()
Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)

IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df['Price'] >= lower_bound) & (df['Price'] <= upper_bound)]



X = df[['Elevator','Floor','Area','Parking','Room','Warehouse','YearOfConstruction','Address_Encoded']]
# X = df.iloc[ : , [0,1,2,3,4,6,7,9,10,11] ]
Y = df['Price']# Target

# print(X.head().to_string())
ss = StandardScaler()
X_rescale = ss.fit_transform(X)

# print(X_rescale)

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train,Y_test = train_test_split(X_rescale , Y, test_size= 0.3,shuffle=True,
                                                   random_state=42)
from sklearn.linear_model import LinearRegression
# print(X_train)

lr = LinearRegression()
lr.fit(X_train, Y_train)
y_pred = lr.predict(X_test)

from sklearn import metrics

mse =mean_squared_error (Y_test ,y_pred)
mae =mean_absolute_error (Y_test ,y_pred)
rmse=np.sqrt(mse)
r2score=r2_score(Y_test,y_pred)


# print(mse)
# print(mse)
# print(rmse)
# print(r2score)


y_residual= Y_test - y_pred
# print(y_residual)


# sns.scatterplot(x=Y_test , y=y_residual)
# plt.axhline(y= 0 , color = 'r' , linestyle ='--' )
# plt.axhline(y= 2 , color = 'r' , linestyle ='--' )
# plt.axhline(y= -2 , color = 'r' , linestyle ='--' )
# plt.show()



final_model = LinearRegression()
final_model.fit(X.values,Y)
# print(final_model.coef_)

# new_data = [[35,25,41]]
#
# print(final_model.predict(new_data))


from joblib import dump, load
dump(final_model,'final_model.pkl')
load_model=load('final_model.pkl')


from tkinter import *
from tkinter import messagebox as msg
from tkinter import ttk
my_form = Tk()
my_form.title('House Price Prediction')
my_form.geometry('800x450')
my_form.resizable(False, False)

def predict_price(event=None):
    event=  None
    area = float(entry_area.get())
    rooms = float(entry_room.get())
    floor = float(entry_floor.get())
    year = float(entry_year.get())

    parking = var_parking.get()
    warehouse = var_warehouse.get()
    elevator = var_elevator.get()

    new_data = [[area, rooms, parking, warehouse, elevator, floor, year]]
    prediction = final_model.predict(new_data)
    msg.showinfo('Result: ', f'Result: {round(final_model.predict(new_data)[0], 2)}')

main_form= ttk.Frame(my_form, padding="20")
main_form.grid(row=0, column=0)

ttk.Label(main_form, text="Area :").grid(row=0, column=0, sticky='w', pady=10)
entry_area = ttk.Entry(main_form, width=20)
entry_area.grid(row=0, column=1, padx=10)

ttk.Label(main_form, text="Room :").grid(row=0, column=2, sticky='w', padx=20)
entry_room = ttk.Entry(main_form, width=20)
entry_room.grid(row=0, column=3)


ttk.Label(main_form, text="Floor :").grid(row=1, column=0, sticky='w', pady=10)
entry_floor = ttk.Entry(main_form, width=20)
entry_floor.grid(row=1, column=1)

ttk.Label(main_form, text="Year Of Construction :").grid(row=1, column=2, sticky='w', padx=20)
entry_year = ttk.Entry(main_form, width=20)
entry_year.grid(row=1, column=3)

var_parking = BooleanVar()
ttk.Label(main_form, text="Parking :").grid(row=2, column=0, sticky='w', pady=15)
ttk.Radiobutton(main_form, text="True", variable=var_parking, value=True).place(x=70, y=105)
ttk.Radiobutton(main_form, text="False", variable=var_parking, value=False).place(x=130, y=105)

var_warehouse = BooleanVar()
ttk.Label(main_form, text="WareHouse :").grid(row=2, column=2, sticky='w', padx=20)
ttk.Radiobutton(main_form, text="True", variable=var_warehouse, value=True).place(x=380, y=105)
ttk.Radiobutton(main_form, text="False", variable=var_warehouse, value=False).place(x=440, y=105)

var_elevator = BooleanVar()
ttk.Label(main_form, text="Elevator :").grid(row=3, column=0, sticky='w', pady=15)
ttk.Radiobutton(main_form, text="True", variable=var_elevator, value=True).place(x=70, y=155)
ttk.Radiobutton(main_form, text="False", variable=var_elevator, value=False).place(x=130, y=155)


btn_predict = ttk.Button(main_form, text="Predict", command=predict_price)
btn_predict.grid(row=4, column=0, pady=30)

ttk.Label(main_form, text="Price :", font=('Arial', 12, 'bold')).grid(row=4, column=1)
lbl_result = ttk.Label(main_form, text="---", font=('Arial', 12, 'bold'))
lbl_result.grid(row=4, column=2, sticky='w')

my_form.bind('<Return>', predict_price)
my_form.mainloop()







