import pandas as pd
import numpy as np

# Create a DataFrame with random values and some NaN values
data = np.random.rand(10, 4)
nan_indices = np.random.choice(range(10), size=(5,), replace=False)
data[nan_indices, np.random.choice(range(4), size=(5,))] = np.nan
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])

# Keep rows with at least 2 NaN values
df_at_least_2_nan = df.dropna(thresh=2)

# Display the original and modified DataFrames
print("Original DataFrame:")
print(df)
print("\nDataFrame with at least 2 NaN values:")
print(df_at_least_2_nan)
