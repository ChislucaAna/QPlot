import matplotlib.pyplot as plt

points = [(1, 2), (3, 4), (5, 1), (6, 7)]

x_values = []
y_values = []

for point in points:
    x_values.append(point[0])
    y_values.append(point[1])

plt.scatter(x_values, y_values, color='blue', marker='o')

for point in points:
    plt.text(point[0], point[1], f'({point[0]}, {point[1]})')

plt.xlabel('Axa Ox')
plt.ylabel('Axa Oy')
plt.title('Puncte in 2D')
plt.grid()
plt.show()
