
import joblib
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
address_encoder = joblib.load("address_encoder.pkl")
import streamlit as st
import pandas as pd
import joblib
import numpy as np
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# بارگذاری مدل‌ها
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
address_encoder = joblib.load("address_encoder.pkl")


st.title("🏠 پیش‌بینی قیمت خانه")

# ورودی‌ها
area = st.number_input("متراژ (m²):", min_value=10, max_value=1000, value=100)
floor = st.number_input("طبقه:", min_value=0, max_value=50, value=1)
room = st.number_input("تعداد اتاق:", min_value=1, max_value=20, value=3)
year = st.number_input("سال ساخت:", min_value=1900, max_value=2030, value=2000)

parking = st.checkbox("پارکینگ")
warehouse = st.checkbox("انباری")
elevator = st.checkbox("آسانسور")

df = pd.read_csv("HouseNew.csv")
address_options = df["Address"].unique().tolist()
address = st.selectbox("آدرس:", address_options)

# پیش‌بینی
if st.button("💰 پیش‌بینی قیمت"):
    addr_encoded = address_encoder.transform([address])[0]
    X = np.array([[int(elevator), floor, area, int(parking), room, int(warehouse), year, addr_encoded]])
    X_scaled = scaler.transform(X)
    price = model.predict(X_scaled)[0]
    st.success(f"💰 قیمت پیش‌بینی‌شده: {price:,.0f} تومان")
