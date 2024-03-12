import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from mpl_toolkits.mplot3d import Axes3D

def biot_savart_magnetic_field(X, Y, Z, I, a, zo):
    c = 1 / (4 * np.pi * 1e-7)
    pi = np.pi

    def integrand(phi, r, theta):
        return (np.cos(phi)) / np.sqrt(a ** 2 + r ** 2 - 2 * a * r * np.sin(theta) * np.cos(phi))

    def I_r_theta_phi(r, theta):
        integral, _ = quad(integrand, 0, 2 * pi, args=(r, theta))
        return integral

    def A_phi(r, theta):
        return (I * a / c) * I_r_theta_phi(r, theta)

    def dA_dtheta(r, theta):
        delta_theta = 1e-6
        return (np.sin(theta + delta_theta) * A_phi(r, theta + delta_theta) - np.sin(theta - delta_theta) * A_phi(r, theta - delta_theta)) / (2 * delta_theta)

    def dA_dr(r, theta):
        delta_r = 1e-6
        return ((r + delta_r) * A_phi(r + delta_r, theta) - (r - delta_r) * A_phi(r - delta_r, theta)) / (2 * delta_r)

    eps = 1e-15
    def B_r(r, theta):
        return (1 / (r * np.sin(theta) + eps)) * dA_dtheta(r, theta)

    def B_theta(r, theta):
        return -(1 / r) * dA_dr(r, theta)

    def B_phi(r, theta):
        return 0

    r = np.sqrt(X ** 2 + Y ** 2 + (Z - zo) ** 2)
    theta = np.arccos((Z - zo) / r)
    phi = np.arctan2(Y, X)

    # Vectorize the necessary functions
    I_r_theta_phi_vec = np.vectorize(I_r_theta_phi)
    dA_dtheta_vec = np.vectorize(dA_dtheta)
    dA_dr_vec = np.vectorize(dA_dr)
    B_r_vec = np.vectorize(B_r)
    B_theta_vec = np.vectorize(B_theta)
    B_phi_vec = np.vectorize(B_phi)

    # Calculate the components of B in spherical coordinates using the vectorized functions
    B_r_value = B_r_vec(r, theta)
    B_theta_value = B_theta_vec(r, theta)
    B_phi_value = B_phi_vec(r, theta)

    B_x_value = np.sin(theta) * np.cos(phi) * B_r_value + np.cos(theta) * np.cos(phi) * B_theta_value - np.sin(phi) * B_phi_value
    B_y_value = np.sin(theta) * np.sin(phi) * B_r_value + np.cos(theta) * np.sin(phi) * B_theta_value + np.cos(phi) * B_phi_value
    B_z_value = np.cos(theta) * B_r_value - np.sin(theta) * B_theta_value

    return np.array([B_x_value, B_y_value, B_z_value])

I = 0.6
a = 1.5
zo1 = 1.0
zo2 = 2.0

x_values = np.linspace(-2 * a, 2 * a, 9)
y_values = np.linspace(-2 * a, 2 * a, 9)
z_values = np.linspace(-2 * a, 2 * a, 9)

X, Y, Z = np.meshgrid(x_values, y_values, z_values, indexing='ij')

B1 = biot_savart_magnetic_field(X, Y, Z, I, a, zo1)
B2 = biot_savart_magnetic_field(X, Y, Z, I, a, zo2)
B_total = B1 + B2




fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

def draw_spiral(ax, zo, a, color='red', num_points=100):
    phi = np.linspace(0, 2 * np.pi, num_points)
    x = a * np.cos(phi)
    y = a * np.sin(phi)
    z = np.ones_like(phi) * zo
    ax.plot(x, y, z, color=color)

draw_spiral(ax, zo1, a)
draw_spiral(ax, zo2, a)

ax.quiver(X, Y, Z, B_total[0], B_total[1], B_total[2], length=a/5, normalize=True, color='b', linewidth=0.5)

ax.set_title('Campo magnético total debido a dos espiras de corriente')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

plt.show()

