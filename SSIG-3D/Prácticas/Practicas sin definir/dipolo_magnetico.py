import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def magnetic_dipole_field(x, y, z, m_x, m_y, m_z):
    mu_0 = 4 * np.pi * 1e-7  # Permeabilidad magnética del vacío
    r = np.sqrt(x**2 + y**2 + z**2)
    r_cubed = r**3

    # Calcular las componentes del campo magnético
    B_x = (3 * x * (x * m_x + y * m_y + z * m_z) - r**2 * m_x) / r_cubed
    B_y = (3 * y * (x * m_x + y * m_y + z * m_z) - r**2 * m_y) / r_cubed
    B_z = (3 * z * (x * m_x + y * m_y + z * m_z) - r**2 * m_z) / r_cubed

    B_x *= mu_0 / (4 * np.pi)
    B_y *= mu_0 / (4 * np.pi)
    B_z *= mu_0 / (4 * np.pi)

    return B_x, B_y, B_z

# Parámetros del dipolo magnético
m_x, m_y, m_z = 0, 0, 1e-6

# Calcular el campo magnético en un espacio 3D
grid_size = 10
x_values = np.linspace(-1, 1, grid_size)
y_values = np.linspace(-1, 1, grid_size)
z_values = np.linspace(-1, 1, grid_size)
X, Y, Z = np.meshgrid(x_values, y_values, z_values)
B_x_values, B_y_values, B_z_values = magnetic_dipole_field(X, Y, Z, m_x, m_y, m_z)

# Graficar las líneas de campo magnético en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Normalizar vectores para que las flechas tengan la misma longitud
magnitude = np.sqrt(B_x_values**2 + B_y_values**2 + B_z_values**2)
B_x_norm = B_x_values / magnitude
B_y_norm = B_y_values / magnitude
B_z_norm = B_z_values / magnitude

ax.quiver(X, Y, Z, B_x_norm, B_y_norm, B_z_norm, length=0.1, color='b', linewidth=0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Líneas de campo magnético de un dipolo')

plt.show()
