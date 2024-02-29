import pandas as pd
import numpy as np

# Create a DataFrame with random values and some NaN values
data = np.random.rand(10, 4)
nan_indices = np.random.choice(range(10), size=(5,), replace=False)
data[nan_indices, np.random.choice(range(4), size=(5,))] = np.nan
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])

# Detect missing values and display True or False
missing_values = df.isna()

# Display the result
print(missing_values)
