import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# Parámetros del problema
#q = 1
#d = 2

q = float(input("Ingrese el valor de la carga puntual (q): "   ))
d = float(input("Ingrese el valor de la distancia (d), de la carga puntual a la superficie de la esfera (se sugiere d< 5): "))
if  d < 0:
    exit(0)
    

R = 1

# Coordenadas de la carga puntual
carga_puntual_pos = np.array([0, 0, d])

# Calcular la carga imagen y su posición
q_imagen = -q * (R / (d - R))
pos_imagen = (R**2 / d) * carga_puntual_pos / np.linalg.norm(carga_puntual_pos)

# Crear una malla esférica
theta, phi = np.mgrid[0:2 * np.pi:100j, 0:np.pi:50j]
x = R * np.sin(phi) * np.cos(theta)
y = R * np.sin(phi) * np.sin(theta)
z = R * np.cos(phi)

# Calcular la densidad de carga en cada punto de la malla
densidad_carga = np.zeros_like(phi)

for i in range(theta.shape[0]):
    for j in range(theta.shape[1]):
        posicion_esfera = np.array([x[i, j], y[i, j], z[i, j]])
        distancia = np.linalg.norm(pos_imagen - posicion_esfera)
        densidad_carga[i, j] = q_imagen / distancia**2

# Normalizar la densidad de carga para la visualización
densidad_carga_norm = (densidad_carga - densidad_carga.min()) / (densidad_carga.max() - densidad_carga.min())

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Igualar la relación de aspecto de los ejes
ax.set_box_aspect([1, 1, 1])

# Desactivar los ejes y la cuadrícula
ax.set_axis_off()
ax.grid(False)

# Graficar la esfera con la densidad de carga
ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=cm.jet(densidad_carga_norm), linewidth=0, alpha=0.5)

# Agregar la carga puntual y la carga imagen
ax.scatter(*carga_puntual_pos, c='red', marker='o', s=50, label='Carga puntual')
ax.scatter(*pos_imagen, c='blue', marker='o', s=50, label='Carga imagen')

# Configurar la gráfica
ax.set_title("Distribución de carga eléctrica en una esfera conductora, debido a una carga puntual")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
# Establecer los límites de los ejes
ax.set_xlim(-R, d)
ax.set_ylim(-R, d)
ax.set_zlim(-R, d)


# Crear la barra de colores
mappable = cm.ScalarMappable(cmap=cm.jet)
mappable.set_array(densidad_carga)
plt.colorbar(mappable, ax=ax, label="Densidad de carga")

# Mostrar la gráfica
plt.show()

