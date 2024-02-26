import matplotlib.pyplot as plt
import numpy as np

# Sample data
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]

# Set up positions for the bars
bar_width = 0.35
index = np.arange(len(groups))

# Create bar plot for men
plt.bar(index, means_men, bar_width, label='Men', color='blue')

# Create bar plot for women, shift positions
plt.bar(index + bar_width, means_women, bar_width, label='Women', color='pink')

# Add labels and title
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(index + bar_width / 2, groups)  # Set x-axis ticks to group names

# Add legend
plt.legend()

# Display the plot
plt.show()
