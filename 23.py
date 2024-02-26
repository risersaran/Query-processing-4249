import matplotlib.pyplot as plt

def draw_line(x_values, y_values, x_label, y_label, title):
    # Plot the line
    plt.plot(x_values, y_values, label='Line')

    # Add labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Show legend
    plt.legend()

    # Display the plot
    plt.show()

# Example usage
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]
x_label = 'X-axis Label'
y_label = 'Y-axis Label'
title = 'Line Plot Example'

draw_line(x_values, y_values, x_label, y_label, title)
