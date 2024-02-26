import matplotlib.pyplot as plt
import numpy as np

# Sample data
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
std_dev_men = [4, 3, 4, 1, 5]
std_dev_women = [3, 5, 2, 3, 3]

# Set up positions for the bars
bar_width = 0.35
index = np.arange(len(groups))

# Create stacked bar plot with error bars
plt.bar(index, means_men, bar_width, yerr=std_dev_men, label='Men', color='blue', capsize=5)
plt.bar(index, means_women, bar_width, yerr=std_dev_women, label='Women', color='pink',
        bottom=means_men, capsize=5)

# Add labels and title
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Stacked Bar Plot with Error Bars')

# Add legend
plt.legend()

# Display the plot
plt.show()
