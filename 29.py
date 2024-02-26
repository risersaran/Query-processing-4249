import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Define different colors for each bar
colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'lightcyan', 'lightpink']

# Create a bar chart with different colors
plt.figure(figsize=(10, 6))
plt.bar(languages, popularity, color=colors)

# Add labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages')

# Display the plot
plt.show()
