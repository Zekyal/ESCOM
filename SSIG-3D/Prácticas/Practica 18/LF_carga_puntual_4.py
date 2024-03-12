import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource
from scipy.integrate import solve_ivp

def electric_field(x, y, z, q, k):
    r = np.sqrt(x**2 + y**2 + z**2)
    Ex = k * q * x / r**3
    Ey = k * q * y / r**3
    Ez = k * q * z / r**3
    return Ex, Ey, Ez

def field_line(t, pos, q, k):
    x, y, z = pos
    Ex, Ey, Ez = electric_field(x, y, z, q, k)
    return [Ex, Ey, Ez]

q = 1e-9
k = 8.9875517923e9

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title("Líneas de flujo y campo eléctrico de una carga puntual\n"
             r"$\vec{E} = \frac{1}{4 \pi \epsilon_0} \frac{q}{|\vec{r}|^2} \hat{r}$")


# Dibuja líneas de flujo y vectores del campo eléctrico
num_streamlines = 45
num_vectors_per_streamline = 5

for i in range(num_streamlines):
    theta = np.random.uniform(0, np.pi)
    phi = np.random.uniform(0, 2 * np.pi)
    x0 = 0.1 * np.sin(theta) * np.cos(phi)
    y0 = 0.1 * np.sin(theta) * np.sin(phi)
    z0 = 0.1 * np.cos(theta)

    sol = solve_ivp(field_line, [0, 5], [x0, y0, z0], args=(q, k), rtol=1e-6, atol=1e-6)
    ax.plot(sol.y[0], sol.y[1], sol.y[2], color='blue', linestyle='dashed')

    # Dibuja vectores del campo eléctrico sobre las líneas de flujo
    num_points = len(sol.y[0])
    vector_indices = np.linspace(0, num_points-1, num_vectors_per_streamline, dtype=int)

    for idx in vector_indices:
        x, y, z = sol.y[0][idx], sol.y[1][idx], sol.y[2][idx]
        Ex, Ey, Ez = electric_field(x, y, z, q, k)
        E = np.sqrt(Ex**2 + Ey**2 + Ez**2)

        epsilon = 1e-9
        ax.quiver(x, y, z, Ex/(E + epsilon), Ey/(E + epsilon), Ez/(E + epsilon), length=0.5, color='red')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
