import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Datos de entrada
I = 0.6  # Valor de la corriente en la espira [carga/tiempo]
#c = 1.0  # c = 4 * pi * epsilon
c = 1 / (4 * np.pi * 1e-7)  # c = 1 / (4 * pi * epsilon), con epsilon = 1e-7 (permeabilidad magnética del vacío)

a = 1.5 # Radio de la espira
pi = np.pi

# Función a integrar
def integrand(phi, r, theta):
    return (np.cos(phi)) / np.sqrt(a ** 2 + r ** 2 - 2 * a * r * np.sin(theta) * np.cos(phi))

# Cálculo de I(r, theta, phi)
def I_r_theta_phi(r, theta):
    integral, _ = quad(integrand, 0, 2 * pi, args=(r, theta))
    return integral

# Calcular A_phi
def A_phi(r, theta):
    return (I * a / c) * I_r_theta_phi(r, theta)

# Calcular las derivadas parciales de A_phi
def dA_dtheta(r, theta):
    delta_theta = 1e-6
    return (np.sin(theta + delta_theta)*A_phi(r, theta + delta_theta) - np.sin(theta -  delta_theta)*A_phi(r, theta - delta_theta)) / (2 * delta_theta)

def dA_dr(r, theta):
    delta_r = 1e-6
    return ((r+ delta_r)*A_phi(r + delta_r, theta) - (r- delta_r)*A_phi(r - delta_r, theta)) / (2 * delta_r)

# Calcular las componentes del campo magnético B
eps = 1e-15
def B_r(r, theta):
    return (1 / (r * np.sin(theta) + eps)) * dA_dtheta(r, theta)

def B_theta(r, theta):
    return -(1 / r) * dA_dr(r, theta)

def B_phi(r, theta):
    return 0

# Crear una malla en coordenadas esféricas
r_values = np.linspace(0.00001, 2 * a, 9)
theta_values = np.linspace(0, np.pi, 8)
phi_values = np.linspace(0, 2 * np.pi, 9)

R, Theta, Phi = np.meshgrid(r_values, theta_values, phi_values, indexing='ij')

# Calcular las componentes de B en cada punto de la malla
B_r_values = np.vectorize(B_r)(R, Theta)
B_theta_values = np.vectorize(B_theta)(R, Theta)
B_phi_values = np.vectorize(B_phi)(R, Theta)

# Crear matriz 3D para guardar los valores de B
B_matrix = np.zeros((len(r_values), len(theta_values), len(phi_values), 3))

# Guardar los valores de B en la matriz 3D
B_matrix[:, :, :, 0] = B_r_values
B_matrix[:, :, :, 1] = B_theta_values
B_matrix[:, :, :, 2] = B_phi_values

# Convertir coordenadas esféricas a cartesianas
X = R * np.sin(Theta) * np.cos(Phi)
Y = R * np.sin(Theta) * np.sin(Phi)
Z = R * np.cos(Theta)

# Convertir componentes de B en coordenadas esféricas a cartesianas
B_x_values = np.sin(Theta) * np.cos(Phi) * B_r_values + np.cos(Theta) * np.cos(Phi) * B_theta_values - np.sin(Phi) * B_phi_values
B_y_values = np.sin(Theta) * np.sin(Phi) * B_r_values + np.cos(Theta) * np.sin(Phi) * B_theta_values + np.cos(Phi) * B_phi_values
B_z_values = np.cos(Theta) * B_r_values - np.sin(Theta) * B_theta_values

# Graficar el campo magnético
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Crear máscara para vectores en el plano YZ (X = 0)
mask = np.isclose(X, 0, atol=1e-8)

# Dibujar los vectores en el plano YZ (X = 0) en negro
ax.quiver(X[mask], Y[mask], Z[mask], B_x_values[mask], B_y_values[mask], B_z_values[mask], length=a/5, normalize=True, color='k', linewidth=0.5)

# Dibujar los vectores que no están en el plano YZ en azul
ax.quiver(X[~mask], Y[~mask], Z[~mask], B_x_values[~mask], B_y_values[~mask], B_z_values[~mask], length=a/5, normalize=True, color='b', linewidth=0.5)



ax.quiver(X, Y, Z, B_x_values, B_y_values, B_z_values, length=a/5, normalize=True, color='b', linewidth=0.5)
ax.set_title('Campo magnético de una espira de corriente')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Graficar la espira en color rojo
print ('a   =', a)
phi_spiral = np.linspace(0, 2 * np.pi, 70)
x_spiral = a * np.cos(phi_spiral)
y_spiral = a * np.sin(phi_spiral)
z_spiral = np.zeros_like(phi_spiral)
ax.plot(x_spiral, y_spiral, z_spiral, color='r', linewidth=2)

# Agregar el plano YZ de color naranja con una transparencia de 0.5
#yz_plane_vertices = np.array([[-2 * a, -2 * a, -2 * a], [-2 * a, 2 * a, -2 * a], [-2 * a, 2 * a, 2 * a], [-2 * a, -2 * a, 2 * a]])
yz_plane_vertices = np.array([[0, -2 * a, -2 * a], [0, 2 * a, -2 * a], [0, 2 * a, 2 * a], [0, -2 * a, 2 * a]])
yz_plane = Poly3DCollection([yz_plane_vertices], alpha=0.5, facecolor='orange')
ax.add_collection3d(yz_plane)


plt.show()
