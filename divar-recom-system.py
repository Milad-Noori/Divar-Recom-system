from tkinter import *
import tkinter as tk
from tkinter import ttk
def print_predict():
    try:
        area = float(area_entry.get())
        floor = int(floor_entry.get())
        room = int(room_entry.get())
        year = int(yearof_construction_entry.get())

        parking = parking_var.get()
        warehouse = were_var.get()
        elevator = elev_var.get()

        address = address_entry.get()

        predicted_price = predict_priced(
            area, floor, room, year,
            parking, warehouse, elevator,
            address
        )

        greting_label.configure(
            text=f"💰 Predicted Price: {predicted_price:,} Toman",
            fg="green"
        )

    except Exception as e:
        greting_label.configure(text="❌ Input error", fg="red")
        print(e)


window = Tk()
window.title("House-price")
def get_state():
    if were_var.get()==1:
        print("Yes")
    else:
        print("No")


def get_state2():
    if parking_var.get()==1:
        print("Yes")
    else:
        print("No")



def get_state3():
    if elev_var.get()==1:
        print("Yes")
    else:
        print("No")


window.geometry("800x600")

Address =Address_label = Label(window, text="Address :")
Address_label.place(x=50, y=60)
address_options = ["Pounak", "Saadat Abad", "Gisha", "Tehranpars"]
address_entry = ttk.Combobox(window, values=address_options, width=37)
address_entry.place(x=200, y=60, height=26)
address_entry.current(0)

Area = Label(window,text = "Area :",padx=15,pady=15)
Area.place(x=50,y=100)
area_entry=Entry(window)
area_entry.place(x=200,y=115,width=250,height=25)


Floor = Label(window,text = "Floor :",padx=15,pady=15)
Floor.place(x=50,y=150)
floor_entry=Entry(window)
floor_entry.place(x=200,y=162,width=250,height=25)

Room= Label(window,text = "Room :",padx=15,pady=15)
Room.place(x=50,y=200)
room_entry=Entry(window)
room_entry.place(x=200,y=212,width=250,height=25)

YearOfConstruction = Label(window,text="YearOfConstruction :",padx=10,pady=10)
YearOfConstruction.place(x=50,y=262)
yearof_construction_entry=Entry(window)
yearof_construction_entry.place(x=200,y=267,width=250,height=25)

parking_var = IntVar()
checkbutton2 = Checkbutton(window,text="Parking",variable=parking_var,onvalue=1, offvalue=0,command=get_state2)
checkbutton2.place( x=100,y=420)


# Warehouse = Label(window,text="Warehouse :",padx=10,pady=10)
# Warehouse.place(x=200,y=365)
were_var = IntVar()
checkbutton1 =Checkbutton(window,text="Warehouse",variable=were_var,onvalue=1, offvalue=0,command=get_state)
checkbutton1.place(x=200,y=420)


elev_var = IntVar()
checkbutton3 = Checkbutton(window,text="Elevator",variable=elev_var,onvalue=1, offvalue=0,command=get_state3)
checkbutton3.place(x=300,y=420)

price= Label(window,text = "🏷️Price :",padx=15,pady=15,font=("Arial",20))
price.place(x=350,y=500)

Button = Button(window,text = "textPredict",padx=20,pady=10,bd=5,command=print_predict)
Button.place(x=50,y=500)
greting_label= Label(window,text="",padx=10,pady=10)
greting_label.place(x=50,y=550)
window.mainloop()
