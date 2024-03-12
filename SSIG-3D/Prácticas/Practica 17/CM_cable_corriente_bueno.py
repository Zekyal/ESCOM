import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp

# Constantes
I = 10  # Corriente en amperios
mu_0 = 4 * np.pi * 1e-7  # Permeabilidad magnética del vacío

# Función para calcular el campo magnético en un punto P(x, y, z)
def magnetic_field(x, y, z):
    rho = np.sqrt(x**2 + y**2)
    B = (mu_0 * I) / (2 * np.pi * rho)
    Bx = -B * y / rho
    By = B * x / rho
    Bz = z * 0
    return Bx, By, Bz

# Crear la figura y el objeto Axes3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Establecer los límites de los ejes
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)

# Inicializar carga ficticia
charge, = ax.plot([], [], [], 'o', color='orange', markersize=6)

# Función de inicialización para la animación
def init():
    charge.set_data([], [])
    charge.set_3d_properties([])
    return charge,

# Función de actualización para la animación
def update(frame):
    z_charge = -2 + 4 * frame / 30
    charge.set_data(0, 0)
    charge.set_3d_properties(z_charge)
    return charge,

# Crear la animación
ani = FuncAnimation(fig, update, frames=30, init_func=init, blit=True, interval=100, repeat=True)

# Vectores del campo magnético (color azul)
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
z = np.linspace(-2, 2, 10)
X, Y, Z = np.meshgrid(x, y, z)
Bx, By, Bz = magnetic_field(X, Y, Z)
ax.quiver(X, Y, Z, Bx, By, Bz, color='b', length=0.2, normalize=True, arrow_length_ratio=0.2)

# Cable infinito (color gris con transparencia)
ax.plot([0, 0], [0, 0], [-2, 2], 'k-', linewidth=5, alpha=0.5, label='Cable infinito')

ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_zlabel('z (m)')
ax.set_title('Animación de campo magnético de un cable infinito transportando corriente I en 3D')
ax.legend()
ax.grid(True)

plt.show()


