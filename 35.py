import matplotlib.pyplot as plt

# Sample data
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create a scatter plot
plt.scatter(math_marks, science_marks, color='blue', alpha=0.7)

# Add labels and title
plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')
plt.title('Scatter Plot: Mathematics vs Science')

# Add a reference line
plt.plot(marks_range, marks_range, linestyle='--', color='gray', alpha=0.5, label='Reference Line')

# Display the plot
plt.legend()
plt.show()
