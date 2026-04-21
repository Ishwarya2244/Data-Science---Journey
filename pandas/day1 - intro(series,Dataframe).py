#pandas series 
import pandas as pd
a=pd.Series([10,20,30,40])
print(a)

print(a[2])

#indexing 
b=pd.Series([10,20,30],index=["a","b","c"])
print(b)

print(b["c"])

#Data Frame = a full table
import pandas as pd
data={
    "Name":["a","b","c"],
    "age":[20,30,40]
}
df=pd.DataFrame(data)
print(df)

#basic
print(df.shape)
print(df.columns)
print(df.head())

 #Your Task Today:

#Filter an array [5, 15, 25, 35, 45] — print only values greater than 20
#Create a Series of 5 city names
#Create a DataFrame with 3 students — Name, Age, Marks
#Print the shape and columns of that DataFrame

import numpy as np
a=np.array([5,15,25,35,45])
print(a[a>20])

import pandas as pd
a=pd.Series(["hosur","Bagalur","therpet","choodapuram","malur"])
print(a)

data={
    "name":["a","b","c"],
    "age":[20,30,40],
    "marks":[90,80,50]
}
df=pd.DataFrame(data)
print(df)

print(df.shape)
print(df.columns)

print(df.head())
print(df.head(1))
print(df.tail())
print(df.tail(2))
