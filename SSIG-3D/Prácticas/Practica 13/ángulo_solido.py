import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Parámetros de la esfera y el cono
radius = 1
theta_cone = np.pi/6   # Ángulo theta respecto al eje Z (30 grados en este caso)
solid_angle = 2 * np.pi * (1 - np.cos(theta_cone))

# Convertir el resultado en múltiplos de π
solid_angle_pi = solid_angle / np.pi

# Simplificar la fracción y mostrar el resultado en múltiplos de π
fraction = sp.Rational(solid_angle_pi).limit_denominator(100)
print("Ángulo sólido subtendido por el cono:", fraction, "π estereorradianes")


##########################################################################################

#print("Ángulo sólido subtendido por el cono:", solid_angle, "estereorradianes")
# Coordenadas esféricas
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
phi, theta = np.meshgrid(phi, theta)

# Coordenadas cartesianas de la esfera
x = radius * np.sin(theta) * np.cos(phi)
y = radius * np.sin(theta) * np.sin(phi)
z = radius * np.cos(theta)

# Coordenadas cilíndricas para el cono
r_cone = np.linspace(0, radius, 100)
cone_phi = np.linspace(0, 2 * np.pi, 100)
r_cone, cone_phi = np.meshgrid(r_cone, cone_phi)

# Coordenadas cartesianas del cono
cone_x = r_cone * np.sin(theta_cone) * np.cos(cone_phi)
cone_y = r_cone * np.sin(theta_cone) * np.sin(cone_phi)
cone_z = r_cone * np.cos(theta_cone)

# Crear y configurar la figura y el objeto Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1])  # Establecer la misma escala en todos los ejes

# Dibujar la esfera con un color azul suave y cierta transparencia
ax.plot_surface(x, y, z, color='lightskyblue', alpha=0.6, rstride=1, cstride=1)

# Dibujar el cono con color gris y cierta transparencia
ax.plot_surface(cone_x, cone_y, cone_z, color='gray', alpha=0.3, rstride=1, cstride=1)

# Máscara para el área intersectada por el cono
mask = theta <= theta_cone

# Coordenadas cartesianas de la intersección
x_intersect = x[mask]
y_intersect = y[mask]
z_intersect = z[mask]

# Dibujar la intersección en color rojo
ax.scatter(x_intersect, y_intersect, z_intersect, color='red', s=1, alpha=1)

# Mostrar el gráfico
plt.show()
