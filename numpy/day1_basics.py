import numpy as np
a=np.array([1,2,3,4,5])
print(a)
print(a+10)
print(a*2)
print(a.mean())
print(a.sum())
print(a.min())
print(a.max())

#2d array
b=np.array([[1,2,3],[4,5,6]])
print(b)
print(b.shape)

#Create an array of numbers 10 to 50
#Find the mean and sum of that array
#Multiply every element by 5

import numpy as np
a=np.array([10,20,30,40,50])
print(a)
print(a*5)
print(a.mean())
print(a.sum())

a=np.arange(10,51,10) #start=10, stop =51 , step = 10
print(a)

b=np.arange(10,51)
print(b)
