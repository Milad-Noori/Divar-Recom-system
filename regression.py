import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import joblib
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('HouseNew.csv')
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

# بارگذاری داده‌ها
df = pd.read_csv("HouseNew.csv")

# ساخت LabelEncoder برای ستون Address
address_encoder = LabelEncoder()
address_encoder.fit(df["Address"])  # فقط روی داده واقعی آموزش بده

# ذخیره encoder برای استفاده بعدی
joblib.dump(address_encoder, "address_encoder.pkl")
df1=pd.DataFrame(data)
print(df1.isnull().sum())

df1["Elevator"] =df1["Elevator"].astype(int)
df1["Parking"] =df1["Parking"].astype(int)
df1["Warehouse"] =df1["Warehouse"].astype(int)


df1["Age"] = 1404 - df1["YearOfConstruction"]
df1["Floor"] = df1["Floor"].fillna(df1["Floor"].median())
df1["Address"] = df1["Address"].fillna("نامشخص")
address_counts = df1["Address"].value_counts()
df1["AddressFrequency"] = df1["Address"].map(address_counts)

print(df1["Address"].unique())
print(df1.head(10).to_string())
from sklearn.preprocessing import LabelEncoder,StandardScaler
le = LabelEncoder()
df1["Address_Encode"] = le.fit_transform(df1["Address"])
print(df1.columns)
print(df1.head(10).to_string())



# x = df1.drop(["Price"], axis=1)
X = df1[['Elevator','Floor','Area','Parking','Room','Warehouse','YearOfConstruction','Address_Encode']]
Y = df1["Price"]

ss = StandardScaler()
X_rescale = ss.fit_transform(X)
print(X_rescale)

X_train , X_test , Y_train , Y_test = train_test_split(X_rescale,Y , test_size=0.2 , random_state=0)

lr =LinearRegression()
lr.fit(X_train,Y_train)
y_pred=lr.predict(X_test)


joblib.dump(lr, "model.pkl")
joblib.dump(ss, "scaler.pkl")
joblib.dump("model.pkl")

print("Model and scaler saved successfully")
