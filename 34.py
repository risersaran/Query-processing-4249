import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)  # Setting seed for reproducibility
num_points = 50
x_values = np.random.randn(num_points)  # Random X values with a normal distribution
y_values = np.random.randn(num_points)  # Random Y values with a normal distribution
sizes = np.random.randint(10, 100, num_points)  # Random sizes between 10 and 100

# Create a scatter plot with balls of different sizes
plt.scatter(x_values, y_values, s=sizes, color='blue', alpha=0.7)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Balls of Different Sizes')

# Display the plot
plt.show()
