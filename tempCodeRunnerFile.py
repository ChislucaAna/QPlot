import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

complex_points = [
    (complex(1, 2), complex(3, 4), 5),
    (complex(2, 1), complex(1, 3), 6),
    (complex(3, 2), complex(5, 1), 7),
    (complex(1, 0), complex(0, 1), 8),
]

# Extract real and imaginary parts
x = [point[0].real for point in complex_points]
y = [point[0].imag for point in complex_points]
z = [point[2] for point in complex_points]  # Real z values

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the points
ax.scatter(x, y, z, color='blue')

# Optionally, label the points
for i, point in enumerate(complex_points):
    ax.text(point[0].real, point[0].imag, point[2], f'{point[0]}', fontsize=9)

# Set axis labels
ax.set_xlabel('Real Part of X')
ax.set_ylabel('Imaginary Part of X')
ax.set_zlabel('Z')

# Set the title
ax.set_title('Complex Points in 3D')

# Show the plot
plt.show()