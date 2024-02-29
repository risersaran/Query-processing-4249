import pandas as pd

# Creating a sample DataFrame
data = {'Country': ['USA', 'Canada', 'France', 'Germany', 'Japan'],
        'BeerServings': [200, 250, 180, 220, 150],
        'WineServings': [100, 90, 200, 150, 40],
        'SpiritServings': [150, 120, 80, 100, 60]}

df = pd.DataFrame(data)

# Define the substring you want to find
substring_to_find = 'an'

# Find the index of rows where the substring appears in the 'Country' column
index_of_substring = df[df['Country'].str.contains(substring_to_find, case=False)].index

# Display the result
print(f"Index of rows containing the substring '{substring_to_find}':")
print(index_of_substring)
