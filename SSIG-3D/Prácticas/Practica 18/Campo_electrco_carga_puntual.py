import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir constantes
k = 9e9  # Constante de Coulomb

# Definir la función que calcula el campo eléctrico
def E(q, r0, x, y, z):
    """
    q: Carga de la partícula en Coulombs.
    r0: Posición de la partícula como una tupla (x, y, z).
    x, y, z: Puntos donde queremos calcular el campo eléctrico.
    """
    den = np.sqrt((x - r0[0])**2 + (y - r0[1])**2 + (z - r0[2])**2)**3
    return k * q * (x - r0[0]) / den, k * q * (y - r0[1]) / den, k * q * (z - r0[2]) / den

# Crear una malla de puntos en el espacio tridimensional
x, y, z = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))

# Crear la figura 3D para ambas cargas
fig = plt.figure(figsize=(12, 6))

# Loop para graficar tanto la carga positiva como la negativa
for i, q in enumerate([1.0, -1.0]):

    # Calcular el campo eléctrico en cada punto de la malla
    Ex, Ey, Ez = E(q, (0, 0, 0), x, y, z)

    # Crear un nuevo subplot para cada carga
    ax = fig.add_subplot(1, 2, i + 1, projection='3d')

    # Dibujar la carga como un punto en el centro
    if q > 0:
        ax.scatter([0], [0], [0], color='red', s=100)
        ax.set_title('Líneas de campo eléctrico de una carga positiva')
    else:
        ax.scatter([0], [0], [0], color='blue', s=100)
        ax.set_title('Líneas de campo eléctrico de una carga negativa')

    # Dibujar las líneas de campo eléctrico
    ax.quiver(x, y, z, Ex, Ey, Ez, length=0.1, normalize=True)

    # Configurar los límites de los ejes
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

# Mostrar la figura
plt.show()
