import pandas as pd

# Creating a sample DataFrame
data = {'Country': ['USA', 'Canada', 'France', 'Germany', 'Japan'],
        'BeerServings': [200, 250, 180, 220, 150],
        'WineServings': [100, 90, 200, 150, 40],
        'SpiritServings': [150, 120, 80, 100, 60]}

df = pd.DataFrame(data)

# Specify the character column for case swapping
column_to_swap = 'Country'

# Swap the cases of the specified character column
df[column_to_swap] = df[column_to_swap].str.swapcase()

# Display the DataFrame after case swapping
print("DataFrame after swapping the cases:")
print(df)
