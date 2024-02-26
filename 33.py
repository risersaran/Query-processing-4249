import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)  # Setting seed for reproducibility
num_points = 100
x_values = np.random.randn(num_points)  # Random X values with a normal distribution
y_values = np.random.randn(num_points)  # Random Y values with a normal distribution

# Create a scatter plot with empty circles
plt.scatter(x_values, y_values, facecolors='none', edgecolors='blue', alpha=0.7)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Empty Circles and Random Distribution')

# Display the plot
plt.show()
