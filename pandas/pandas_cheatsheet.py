df.head()              # first 5 rows
df.tail()              # last 5 rows
df.shape               # rows, columns
df.columns             # column names
df.info()              # data types
df.describe()          # statistics
df.isnull().sum()      # missing values
df["col"].unique()     # unique values
df["col"].value_counts() # count each value
df[df["col"] > value]  # filter
df.sort_values("col")  # sort
df["col"].mean()       # average
df["col"].max()        # maximum
df["col"].min()        # minimum
idxmax()   # to print most highest count 
# instead of this 
for x in arr:
    if x % 2 == 0:
        print(x)

# But also know the NumPy way
print(arr[arr % 2 == 0])  # one line — faster!
