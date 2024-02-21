import pandas as pd
import matplotlib.pyplot as plt

# Example data creation (replace this with your actual data)
data = {
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
    'Trading_Volume': [1000000, 1200000, 950000, 1100000, 1050000],
}

stock_data = pd.DataFrame(data)

# Convert 'Date' column to datetime format
stock_data['Date'] = pd.to_datetime(stock_data['Date'])

# Filter data between two specific dates
start_date = '2022-01-01'
end_date = '2022-01-04'
filtered_data = stock_data[(stock_data['Date'] >= start_date) & (stock_data['Date'] <= end_date)]

# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(filtered_data['Date'], filtered_data['Trading_Volume'], color='skyblue')
plt.title('Trading Volume of Alphabet Inc. Stock between {} and {}'.format(start_date, end_date))
plt.xlabel('Date')
plt.ylabel('Trading Volume')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
