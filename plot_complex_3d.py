import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

z1 = complex(2, 3) 
z2 = complex(4, -1)


x_real = [z1.real, z2.real]
y_real = [z1.imag, z2.imag]
z_imag = [0, 0]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x_real, [0, 0], y_real, marker='o', color='b')

ax.set_xlabel('Parte Reala X')
ax.set_ylabel('Parte Reala Y')
ax.set_zlabel('PArte Imaginara')

ax.set_title('REprezentare puncte complexe in sistem 3D')
ax.legend()

plt.show()


