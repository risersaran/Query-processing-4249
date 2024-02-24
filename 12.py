import pandas as pd
import numpy as np

# Create a DataFrame with random values
data = np.random.rand(10, 4)
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])

# Create a style function to set background color to black and font color to yellow
def style_background_yellow_font_black(val):
    return 'background-color: black; color: yellow'

# Apply the style function to the entire DataFrame
styled_df = df.style.apply(lambda x: x.applymap(style_background_yellow_font_black))

# Display the styled DataFrame
styled_df
