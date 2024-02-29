import pandas as pd

# Creating a sample DataFrame
data = {'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'School Code': ['S001', 'S002', 'S001', 'S003', 'S002'],
        'Score': [85, 90, 88, 78, 92]}

df = pd.DataFrame(data)

# Splitting the DataFrame into groups based on 'School Code'
grouped_df = df.groupby('School Code')

# Displaying the type of GroupBy object
print("Type of GroupBy object:", type(grouped_df))

# Displaying the groups (for demonstration purposes)
for group_name, group_data in grouped_df:
    print("\nGroup:", group_name)
    print(group_data)
