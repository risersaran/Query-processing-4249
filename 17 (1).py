import pandas as pd

# Creating a sample DataFrame
data = {'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'School Code': ['S001', 'S002', 'S001', 'S003', 'S002'],
        'Age': [20, 22, 21, 19, 23]}

df = pd.DataFrame(data)

# Grouping by 'School Code' and calculating mean, min, and max age for each school
result = df.groupby('School Code')['Age'].agg(['mean', 'min', 'max'])

# Displaying the result
print(result)
