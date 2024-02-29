import pandas as pd

# Assuming you have a World alcohol consumption dataset (replace 'your_dataset.csv' with the actual file name)
# df = pd.read_csv('your_dataset.csv')

# Creating a sample DataFrame for demonstration purposes
data = {'Country': ['USA', 'Canada', 'France', 'Germany', 'Japan'],
        'BeerServings': [200, 250, 180, 220, 150],
        'WineServings': [100, 90, 200, 150, 40],
        'SpiritServings': [150, 120, 80, 100, 60]}

df = pd.DataFrame(data)

# Displaying the dimensions (shape) of the dataset
print("Dimensions of the dataset:", df.shape)

# Extracting and displaying the column names
print("\nColumn names:")
print(df.columns)
