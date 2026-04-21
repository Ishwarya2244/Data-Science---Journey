#! indexing
import numpy as np

a = np.array([10, 20, 30, 40, 50])

# Accessing single element
print(a[0])    # 10 — first element
print(a[1])    # 20 — second element
print(a[-1])   # 50 — last element
print(a[-2])   # 40 — second last

#! slicing
a = np.array([10, 20, 30, 40, 50])

print(a[1:4])   # [20 30 40] — index 1 to 3
print(a[:3])    # [10 20 30] — first 3 elements
print(a[2:])    # [30 40 50] — from index 2 to end
print(a[::2])   # [10 30 50] — every 2nd element

#! 2d arrays
b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(b.shape)     # (3, 3) — 3 rows, 3 columns
print(b[0])        # [1 2 3] — first row
print(b[1][2])     # 6 — row 1, column 2
print(b[2][0])     # 7 — row 2, column 0

#! useful func
a = np.array([10, 20, 30, 40, 50])

print(np.sqrt(a))     # square root of each element
print(np.zeros(5))    # [0. 0. 0. 0. 0.]
print(np.ones(5))     # [1. 1. 1. 1. 1.]
print(np.arange(1, 11))  # [1 2 3 4 5 6 7 8 9 10]

# task
import numpy as np
a=np.array([5,10,15,20,25,30])
print(a[2])
print(a[1:4])
print(a[::2])

#2 d array 
b=np.array([[0,1,2],[3,4,5]])
print(b.shape)

#print the square root
c=np.array([4,9,16,25])
print(np.sqrt(c))
