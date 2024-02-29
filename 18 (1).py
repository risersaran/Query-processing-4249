import pandas as pd

# Creating a sample DataFrame
data = {'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank'],
        'School Code': ['S001', 'S002', 'S001', 'S003', 'S002', 'S001'],
        'Class': ['A', 'B', 'A', 'C', 'B', 'A'],
        'Score': [85, 90, 88, 78, 92, 95]}

df = pd.DataFrame(data)

# Grouping by 'School Code' and 'Class'
grouped_df = df.groupby(['School Code', 'Class'])

# Displaying the groups (for demonstration purposes)
for group_name, group_data in grouped_df:
    print("\nGroup:", group_name)
    print(group_data)
