import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Create multiple subplots
plt.figure(figsize=(10, 8))

# Plot 1
plt.subplot(3, 1, 1)
plt.plot(x, y1, label='sin(x)', color='blue')
plt.title('Plot 1: sin(x)')
plt.legend()

# Plot 2
plt.subplot(3, 1, 2)
plt.plot(x, y2, label='cos(x)', color='green')
plt.title('Plot 2: cos(x)')
plt.legend()

# Plot 3
plt.subplot(3, 1, 3)
plt.plot(x, y3, label='tan(x)', color='red')
plt.title('Plot 3: tan(x)')
plt.legend()

# Adjust layout for better spacing
plt.tight_layout()

# Display the plots
plt.show()
