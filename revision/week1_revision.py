Revision 1 — NumPy
Try to write these from memory:
1. Import numpy
2. Create an array of [10, 20, 30, 40, 50]
3. Print mean, sum, max, min
4. Filter values greater than 25
5. Create a 2D array of 2 rows and 3 columns
6. Print its shape
7. Generate 5 random numbers between 1 and **100**


import numpy as np
arr=np.array([10,20,30,40,50])
print(arr.mean())
print(arr.max())
print(arr.sum())
print(arr.min())

print(arr[arr>25])

arr2=np.array([[1,2,3],[4,5,6]])
print(arr2.shape)

rand=np.random.randint(1,100,5)
print(rand)

Revision 2 — Pandas
1. Import pandas
2. Create a DataFrame with 4 students
   — Name, Age, City, Marks
3. Print head, shape, columns
4. Check missing values
5. Filter students with marks > 75
6. Add a Result column — Pass if marks > 50 else Fail
7. Find average marks
8. Sort by marks highest to lowest

import pandas as pd
data={
    'Name':['a','b','c','d'],
    'Age':[20,30,40,60],
    'City':['j','k','l','m'],
    'Marks':[90,80,70,800],
}
df=pd.DataFrame(data)
print(df)

print(df.shape)
print(df.head())
print(df.columns)

print(df.isnull().sum())

print(df[df['Marks']>75])

df['Result']=df['Marks'].apply(lambda x: 'Pass' if x > 50 else 'Fail')
print(df)

print(df['Marks'].mean())

print(df.sort_values(by='Marks',ascending=False))
