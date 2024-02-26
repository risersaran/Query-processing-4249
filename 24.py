import pandas as pd
import matplotlib.pyplot as plt

# Sample Financial data
data = {
    'Date': ['10-03-16', '10-04-16', '10-05-16', '10-06-16', '10-07-16'],
    'Open': [774.25, 776.030029, 779.309998, 779, 779.659973],
    'High': [776.065002, 778.710022, 782.070007, 780.47998, 779.659973],
    'Low': [769.5, 772.890015, 775.650024, 775.539978, 770.75],
    'Close': [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y')

# Plot line charts for Open, High, Low, and Close prices
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Open'], label='Open', marker='o')
plt.plot(df['Date'], df['High'], label='High', marker='o')
plt.plot(df['Date'], df['Low'], label='Low', marker='o')
plt.plot(df['Date'], df['Close'], label='Close', marker='o')

# Set labels and title
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Financial Data of Alphabet Inc.')

# Show legend
plt.legend()

# Display the plot
plt.show()
