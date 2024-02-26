import matplotlib.pyplot as plt

def plot_lines(x_values, y_values_list, labels, colors, widths):
    # Plot each line
    for i in range(len(y_values_list)):
        plt.plot(x_values, y_values_list[i], label=labels[i], color=colors[i], linewidth=widths[i])

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Multiple Lines with Legends')

    # Show legend
    plt.legend()

    # Display the plot
    plt.show()

# Example usage
x_values = [1, 2, 3, 4, 5]

# Two lines with different colors, widths, and labels
y_values_list = [
    [2, 4, 6, 8, 10],  # Line 1
    [1, 3, 5, 7, 9]    # Line 2
]

labels = ['Line 1', 'Line 2']
colors = ['blue', 'red']
widths = [2, 3]

plot_lines(x_values, y_values_list, labels, colors, widths)
