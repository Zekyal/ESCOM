import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parámetros
r = 1.0  # Radio de la trayectoria
mass = 1.0  # Masa del objeto
num_points = 250  # Número de puntos en la trayectoria
interval = 0.01  # Intervalo de tiempo entre puntos
t = np.linspace(0, 2*np.pi, num_points)  # Parámetro t para generar la trayectoria

# Trayectoria en coordenadas cartesianas
x = r * np.cos(t)
y = r * np.sin(t)
z = np.zeros_like(t)

# Vectores de velocidad tangenciales
vel_x = -r * np.sin(t)
vel_y = r * np.cos(t)
vel_z = np.zeros_like(t)

# Vectores de fuerza centrífuga
f_cent_x = -((mass / (r*r)) * (vel_x**2 + vel_y**2)) * np.cos(t)
f_cent_y = -((mass / (r*r)) * (vel_x**2 + vel_y**2)) * np.sin(t)
f_cent_z = np.zeros_like(t)

# Crear la figura y el objeto de la animación
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1])  # Aspecto cuadrado para la caja
ax.set_xlim(-1.5*r, 1.5*r)
ax.set_ylim(-1.5*r, 1.5*r)
ax.set_zlim(-1.5*r, 1.5*r)
ax.set_xlabel('Posición_X')
ax.set_ylabel('Posición_Y')
ax.set_zlabel('Posición_Z')
ax.set_title('Movimiento Circular Uniforme')

# Línea de la trayectoria
line, = ax.plot([], [], [], color='black', linestyle='--')

# Actualizar la animación en cada frame
def update(frame):
    ax.cla()  # Borrar el frame anterior
    ax.set_box_aspect([1, 1, 1])  # Aspecto cuadrado para la caja
    ax.quiver(x[frame], y[frame], z[frame], vel_x[frame], vel_y[frame], vel_z[frame], color='red', label=' -> Vector de velocidad')
    ax.quiver(x[frame], y[frame], z[frame], f_cent_x[frame], f_cent_y[frame], f_cent_z[frame], color='blue', label=' -> Fuerza centrípeta')
    ax.set_xlim(-1.5*r, 1.5*r)
    ax.set_ylim(-1.5*r, 1.5*r)
    ax.set_zlim(-1.5*r, 1.5*r)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Movimiento Circular Uniforme')
    # Subtítulos en LaTeX
    ax.text2D(0.05, 0.95, r'$\vec{r}(t) = r(\cos(t), \sin(t))$', transform=ax.transAxes, fontsize=10)
    ax.text2D(0.05, 0.90, r'$\vec{v}(t) = v(t)(-\sin(t), \cos(t))$', transform=ax.transAxes, fontsize=10)
    ax.text2D(0.05, 0.85, r'$\vec{F}_c = \frac{m \cdot v^2}{r^2}(-\cos(t), -\sin(t))$', transform=ax.transAxes, fontsize=10)
    ax.legend()

    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])

    ax.plot(x[:frame], y[:frame], z[:frame], color='black')

# Generar la animación
ani = FuncAnimation(fig, update, frames=num_points, interval=interval*1000)

# Mostrar la animación
plt.show()
