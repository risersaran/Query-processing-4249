import pandas as pd
import matplotlib.pyplot as plt

# Example data creation (replace this with your actual data)
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'Trading_Volume': [1000000, 1200000, 950000, 1100000, 1050000],
    'Stock_Price': [1200, 1210, 1195, 1225, 1230],
}

stock_data = pd.DataFrame(data)

# Convert 'Date' column to datetime format
stock_data['Date'] = pd.to_datetime(stock_data['Date'])

# Filter data between two specific dates
start_date = '2022-01-01'
end_date = '2022-01-04'
filtered_data = stock_data[(stock_data['Date'] >= start_date) & (stock_data['Date'] <= end_date)]

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(filtered_data['Stock_Price'], filtered_data['Trading_Volume'], color='orange')
plt.title('Scatter Plot of Trading Volume and Stock Prices of Alphabet Inc. Stock')
plt.xlabel('Stock Price')
plt.ylabel('Trading Volume')
plt.grid(True)
plt.show()
