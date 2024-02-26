import matplotlib.pyplot as plt
import numpy as np

# Generate random data for three groups
np.random.seed(42)  # Setting seed for reproducibility

# Group 1
group1_heights = np.random.normal(170, 10, 30)  # Mean=170, Standard deviation=10
group1_weights = np.random.normal(65, 5, 30)    # Mean=65, Standard deviation=5

# Group 2
group2_heights = np.random.normal(160, 8, 30)   # Mean=160, Standard deviation=8
group2_weights = np.random.normal(60, 6, 30)    # Mean=60, Standard deviation=6

# Group 3
group3_heights = np.random.normal(180, 12, 30)  # Mean=180, Standard deviation=12
group3_weights = np.random.normal(75, 8, 30)    # Mean=75, Standard deviation=8

# Create a scatter plot for three groups
plt.scatter(group1_heights, group1_weights, label='Group 1', color='blue', alpha=0.7)
plt.scatter(group2_heights, group2_weights, label='Group 2', color='green', alpha=0.7)
plt.scatter(group3_heights, group3_weights, label='Group 3', color='red', alpha=0.7)

# Add labels and title
plt.xlabel('Heights (cm)')
plt.ylabel('Weights (kg)')
plt.title('Scatter Plot: Heights vs Weights for Three Groups')

# Add legend
plt.legend()

# Display the plot
plt.show()
