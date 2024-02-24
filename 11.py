import pandas as pd
import numpy as np

# Create a DataFrame with random values
data = np.random.rand(10, 4)

# Convert some values to NaN
nan_indices = np.random.choice(range(10), size=(5,), replace=False)
data[nan_indices, np.random.choice(range(4), size=(5,))] = np.nan

# Create a DataFrame with the random values
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])

# Create a function to highlight NaN values in red
def highlight_null(val):
    color = 'red' if pd.isnull(val) else ''
    return f'background-color: {color}'

# Apply the function to the DataFrame
styled_df = df.style.apply(lambda x: x.applymap(highlight_null))

# Display the styled DataFrame
styled_df

