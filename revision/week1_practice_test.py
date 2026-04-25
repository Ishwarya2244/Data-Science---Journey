**Section 1 — NumPy (4 questions)**

Q1. Create an array of numbers from 1 to 20 using arange. Print only even numbers from that array.

import numpy as np
arr=np.arange(1,20)
for x in arr:
  if x % 2==0:
    print(x)

Q2. Create a 2D array of 3 rows and 3 columns. Print:

Its shape
The second row
The element at row 2, column 1

arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2.shape)
print(arr2[1])
print(arr2[1][0])

Q3. Create two arrays:
a = [10, 20, 30, 40, 50]
b = [5, 10, 15, 20, 25]

Add them together
Multiply them together
Find which elements in a are greater than 25

a = [10, 20, 30, 40, 50]
b = [5, 10, 15, 20, 25]
c=np.array([10, 20, 30, 40, 50])
d=np.array([5, 10, 15, 20, 25])
print(c+d)
print(c*d)
print(c[c>25])

Q4. Generate 10 random numbers between 50 and 100. Find their mean, max and min.

rand=np.random.randint(50,100,10)
print(rand.mean())
print(rand.max())
print(rand.min())

**Section 2 — Pandas (6 questions)**

Q5. Create this DataFrame yourself:
Employee Dataset:
- Name: Raj, Priya, Kiran, Meena, Arjun
- Department: HR, IT, Finance, IT, HR
- Salary: 45000, 72000, 58000, 68000, 51000
- Experience: 2, 5, 3, 4, 2

import pandas as pd
data={
    'Name': ['Raj', 'Priya', 'Kiran', 'Meena','Arjun'],
'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
'Salary': [45000, 72000, 58000, 68000, 51000],
'Experience':[ 2, 5, 3, 4, 2]
}
df=pd.DataFrame(data)
print(df)


Q6. From that DataFrame:

Print shape and columns
Print first 3 rows
Check missing values

print(df.shape)
print(df.columns)
print(df.head(3))
print(df.isnull().sum())

Q7. Filter and find:

Employees with salary greater than 60000
Employees in IT department
Employees with experience greater than 3

print(df[df['Salary']>60000])

print(df[df['Department']=='IT'])

print(df[df['Experience']>3])

Q8. Add a new column called "Level":

If salary > 60000 → "Senior"
Else → "Junior"

df['Level']=df['Salary'].apply(lambda x : 'Senior' if x > 60000 else 'Junior' )
print(df)

Q9. Find:

Average salary
Highest salary
Which department appears most (hint: value_counts)

print(df['Salary'].mean())
print(df['Salary'].max())
print(df['Department'].value_counts().idxmax())


Q10. Sort employees by salary highest to lowest and print top 3.

sorted_df = df.sort_values(by='Salary', ascending=False)
print(sorted_df.head(3))
