import numpy as np 
#filtering
a=np.array([70,4,3,2,21,90])
print(a[a>5])

#replacing values 
a[a==4]=10000
print(a)

#random values
a=np.random.randint(20,50,5)
print(a)

a=np.random.randint(1,10000,20)
print(a)

#random values
a=np.random.randint(20,50,5)
print(a)

arr=np.array([0,1,2,3,4,5])
arr[arr==5]=90
print(arr)

print(arr[arr>10])
