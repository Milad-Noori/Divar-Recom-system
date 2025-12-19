import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# df.shape()
# df.head()
# df.describe()
# df.innull().sum()
data = pd.read_csv("HouseNew.csv")
df1 = pd.DataFrame(data)
df1.isnull().sum()
print(df1)
# X_test,Y_test , X_train,Y_train = train_test_split(X,Y ,test_size = 0.2, random_state = 0)
# lr=LinearRegression()
# lr.fit(Y_tesst,Y_train)
# y_pred =lr.predict(X_test)