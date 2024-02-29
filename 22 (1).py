import matplotlib.pyplot as plt

# Sample data
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]

# Plotting the line
plt.plot(x_values, y_values, label='Line Plot')

# Adding labels to the axes
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')

# Adding a title to the plot
plt.title('Line Plot Example')

# Displaying the legend
plt.legend()

# Displaying the plot
plt.show()
