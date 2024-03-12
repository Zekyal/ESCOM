import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Parámetros
R = 1.0  # Radio de la esfera

q = float(input("Ingrese el valor de la carga puntual (q): "))
d = float(input("Ingrese el valor de la distancia (d), de la carga puntual a la carga imagen (se sugiere d< 5): "))
if d < 0:
    exit(0)
if d == R:
    print(' La carga externa (inductora) está sobre la superficie : utilice d > R = 1.')

# Malla esférica
phi, theta = np.mgrid[0:2 * np.pi:100j, 0:np.pi:50j]
x = R * np.sin(theta) * np.cos(phi)
y = R * np.sin(theta) * np.sin(phi)
z = R * np.cos(theta)

# Densidad de carga en función de theta
def densidad_carga(theta, R, d, q):
    return -q * (d**2 - R**2) / (4 * np.pi * R * (R**2 + d**2 - 2 * R * d * np.cos(theta))**(3/2))

# Calcular la densidad de carga en cada punto de la malla
densidad_carga = densidad_carga(theta, R, d, q)

# Coordenadas de la carga puntual
carga_puntual_pos = np.array([0, 0, d])

# Calcular la carga imagen y su posición
q_imagen = -q * (R / d)
pos_imagen = (R**2 / d) * carga_puntual_pos / np.linalg.norm(carga_puntual_pos)

# Crear el objeto mapeable de escalares con los límites correctos
sm = cm.ScalarMappable(cmap=cm.jet, norm=plt.Normalize(vmin=densidad_carga.min(), vmax=densidad_carga.max()))
sm.set_array([])

# Graficar la esfera con la densidad de carga en colores
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=sm.to_rgba(densidad_carga), linewidth=0, antialiased=False, alpha=0.5)

# Dibujar la carga externa y la carga imagen
ax.scatter(*carga_puntual_pos, c='red', marker='o', s=100, label='Carga externa')
ax.scatter(*pos_imagen, c='blue', marker='o', s=100, label='Carga imagen')

# Desactivar los ejes y la cuadrícula
ax.set_axis_off()
ax.grid(False)

# Ajustes del gráfico
ax.set_title('Densidad de carga en la superficie de una esfera conductora  [C/m**2]')
ax.set_title(r'$\sigma(\theta) = \frac{-q(d^2 - R^2)}{4 \pi R (R^2 + d^2 - 2Rd \cos(\theta))^{3/2}}$', fontsize=14, pad=20, loc='center')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Establecer los límites de los ejes
ax.set_xlim(-R, d)
ax.set_ylim(-R, d)
ax.set_zlim(-R, d)

# Barra de colores
cbar = fig.colorbar(sm, ax=ax, shrink=0.7, aspect=5)
cbar.set_label('Densidad de carga C/m**2')

plt.show()

