import pandas as pd
import matplotlib.pyplot as plt

# Assuming your data is in a DataFrame named stock_data
# Ensure that your DataFrame has a 'Date' column and a 'Stock_Price' column

# Example data creation (replace this with your actual data)
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'Stock_Price': [1200, 1210, 1195, 1225, 1230],
}

stock_data = pd.DataFrame(data)

# Convert 'Date' column to datetime format
stock_data['Date'] = pd.to_datetime(stock_data['Date'])

# Filter data between two specific dates
start_date = '2022-01-01'
end_date = '2022-01-04'
filtered_data = stock_data[(stock_data['Date'] >= start_date) & (stock_data['Date'] <= end_date)]

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Date'], filtered_data['Stock_Price'], marker='o', linestyle='-')
plt.title('Alphabet Inc. Stock Prices between {} and {}'.format(start_date, end_date))
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.grid(True)
plt.show()
