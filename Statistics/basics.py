import numpy as np

data = [10, 20, 30, 40, 50]

variance = np.var(data)
std = np.std(data)

print("Variance:", variance)
print("Standard Deviation:", std)

🎯 Your Task Today:
pythonscores = [45, 78, 92, 65, 88, 72, 55, 90, 43, 88]

Find mean, median and mode of scores
Find variance and standard deviation
Create a DataFrame with 5 students and 3 subject marks
Use describe() on the DataFrame
Answer this: which subject has highest std? What does that mean?

import numpy as np
import pandas as pd
from scipy import stats
scores = [45, 78, 92, 65, 88, 72, 55, 90, 43, 88]
print(np.mean(scores))
print(np.median(scores))
print(stats.mode(scores))
print(np.var(scores))
print(np.std(scores))

data={
    'Name':['A','B','C','D','E'],
    'Maths':[90,80,60,40,50],
    'Tamil':[99,40,55,60,79],
    'Science':[98,78,99,95,88]
}
df=pd.DataFrame(data)
print(df)
print(df.describe())


print(df['Maths'].mean())


print(df[['Maths','Tamil','Science']].std())

#SubjectStdAction
#Tamil=22.8 Need extra attention — students are at very different levels
#Maths=20.7 Some weak students need help
#Science=8.7 Class is doing well consistently

#low std== consistent , predictable , good data
# high std == mixed , unpredictable,needs improvement
