import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Constantes
I = 10  # Corriente en amperios
mu_0 = 4 * np.pi * 1e-7  # Permeabilidad magnética del vacío

def magnetic_field(x, y, z, current_direction):
    rho1 = np.sqrt((x - 1)**2 + y**2)  # Distancia al primer cable
    rho2 = np.sqrt((x + 1)**2 + y**2)  # Distancia al segundo cable

    # Campo magnético generado por el primer cable
    B1 = (mu_0 * I) / (2 * np.pi * rho1)
    B1x = -B1 * y / rho1
    B1y = B1 * (x - 1) / rho1
    B1z = z * 0

    # Campo magnético generado por el segundo cable
    B2 = (mu_0 * I * current_direction) / (2 * np.pi * rho2)
    B2x = -B2 * y / rho2
    B2y = B2 * (x + 1) / rho2
    B2z = z * 0

    # Campo magnético total
    Bx = B1x + B2x
    By = B1y + B2y
    Bz = B1z + B2z

    return Bx, By, Bz

def plot_magnetic_field(current_direction):
    # Generar una malla de puntos para evaluar el campo magnético
    x = np.linspace(-3, 3, 10)
    y = np.linspace(-3, 3, 10)
    z = np.linspace(-2, 2, 10)
    X, Y, Z = np.meshgrid(x, y, z)

    # Calcular el campo magnético en cada punto de la malla
    Bx, By, Bz = magnetic_field(X, Y, Z, current_direction)

    # Visualizar los cables, las líneas de flujo y los vectores del campo magnético en 3D
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Vectores del campo magnético (color azul)
    ax.quiver(X, Y, Z, Bx, By, Bz, color='b', length=0.2, normalize=True, arrow_length_ratio=0.2)

    # Cables infinitos (color gris con transparencia)
    ax.plot([1, 1], [0, 0], [-2, 2], 'k-', linewidth=5, color=(0.5, 0.5, 0.5, 0.5), label='Cable infinito 1')
    ax.plot([-1, -1], [0, 0], [-2, 2], 'k-', linewidth=5, color=(0.5, 0.5, 0.5, 0.5), label='Cable infinito 2')

    ax.grid(True)
    
    # Animación de carga en movimiento (color naranja)
   
    charge_positions = np.linspace(-2, 2, 100)

#    def update_charge_position(num, charge, current_direction):
#        charge.set_data([current_direction * (-1)**num * -1, 0])
#        charge.set_3d_properties(charge_positions[num])
#        return charge,

    def update_charge_position(num, charge1, charge2, current_direction):
        charge1.set_data([-1, 0])
        charge1.set_3d_properties(charge_positions[num])
        charge2.set_data([1, 0])
        charge2.set_3d_properties(charge_positions[num] * current_direction)
        return charge1, charge2,

    charge1, = ax.plot([-1], [0], [0], 'o', markersize=8, color='orange', label='Carga en movimiento (Cable 1)')
    charge2, = ax.plot([1], [0], [0], 'o', markersize=8, color='orange', label='Carga en movimiento (Cable 2)')

    ani = animation.FuncAnimation(fig, update_charge_position, len(charge_positions), fargs=(charge1, charge2, current_direction), interval=50, blit=True)

    #ani = animation.FuncAnimation(fig, update_charge_position, len(charge_positions), fargs=(charge1, current_direction), interval=50, blit=True)

    # Ajustar la leyenda para incluir la carga en movimiento
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[:3], labels[:3])

    plt.show()

current_direction = 1  # 1 para la misma dirección, -1 para direcciones opuestas
plot_magnetic_field(current_direction)


