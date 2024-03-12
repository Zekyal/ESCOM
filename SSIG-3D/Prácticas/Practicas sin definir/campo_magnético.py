import numpy as np
import matplotlib.pyplot as plt

def magnetic_dipole_field(x, y, m):
    """
    Calcula el campo magnético de un dipolo magnético en el plano XY.
    :param x: Coordenada x en metros.
    :param y: Coordenada y en metros.
    :param m: Momento magnético en Am².
    :return: Componentes Bx y By del campo magnético en teslas.
    """
    mu_0 = 4 * np.pi * 10 ** -7
    r = np.sqrt(x ** 2 + y ** 2)
    r_cubed = r ** 3
    factor = (mu_0 / (4 * np.pi * r_cubed))

    B_x = 3 * x * y * factor
    B_y = (3 * y ** 2 - r ** 2) * factor

    return B_x, B_y

# Parámetros del dipolo magnético
m = 1e-6  # Momento magnético en Am²

# Calcular el campo magnético en un plano XY
grid_size = 20
x_values = np.linspace(-1, 1, grid_size)
y_values = np.linspace(-1, 1, grid_size)
X, Y = np.meshgrid(x_values, y_values)
B_x_values = np.zeros((grid_size, grid_size))
B_y_values = np.zeros((grid_size, grid_size))

for i in range(grid_size):
    for j in range(grid_size):
        x, y = X[i, j], Y[i, j]
        B_x, B_y = magnetic_dipole_field(x, y, m)
        B_x_values[i, j] = B_x
        B_y_values[i, j] = B_y

# Graficar las líneas de campo magnético
fig, ax = plt.subplots()

# Líneas de flujo
ax.streamplot(X, Y, B_x_values, B_y_values, color='blue', linewidth=0.5, density=2, arrowstyle='->', arrowsize=1)

# Configurar el gráfico
ax.set_xlabel("Posición en x (m)")
ax.set_ylabel("Posición en y (m)")
ax.set_title("Líneas de campo magnético de un dipolo magnético")
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal', 'box')
ax.grid()

# Mostrar el gráfico
plt.show()
