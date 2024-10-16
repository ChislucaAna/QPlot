import matplotlib.pyplot as plt
from domain import Complex
from mpl_toolkits.mplot3d import Axes3D

complex_points = [
    (Complex(1, 2), Complex(3, 4), 5), #Z AICI E MODULUL celui deal doilea nr(y)
    (Complex(2, 1), Complex(1, 3), 6),
    (Complex(3, 2), Complex(5, 1), 7),
    (Complex(1, 0), Complex(0, 1), 8),
]

x = [point[0].real for point in complex_points] #partea reala coordonata OX
y = [point[0].imag for point in complex_points] #partea IMG coodonata OX
z = [point[2] for point in complex_points] #MODULUL NR COMPLEX PT AXA OY

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, color='blue')

for i, point in enumerate(complex_points):
    ax.text(point[0].real, point[0].imag, point[2], f'{point[0]}', fontsize=9)

ax.set_xlabel('Real Part of X')
ax.set_ylabel('Imaginary Part of X')
ax.set_zlabel('Z')
ax.set_title('Complex Points in 3D')
plt.show()

