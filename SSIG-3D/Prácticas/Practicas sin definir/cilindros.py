import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir coordenadas cartesianas
x = 1
y = 2
z = 3

# Convertir a coordenadas cilíndricas
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)
h = z

# Crear malla de coordenadas cilíndricas
theta_vals = np.linspace(0, 2*np.pi, 50)
z_vals = np.linspace(0, h, 50)
theta_vals, z_vals = np.meshgrid(theta_vals, z_vals)
r_vals = np.ones_like(theta_vals) * r
x_vals = r_vals * np.cos(theta_vals)
y_vals = r_vals * np.sin(theta_vals)

# Crear figura y ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar cilindro
ax.plot_surface(x_vals, y_vals, z_vals, alpha = 0.5, color= 'tomato')

# Dibujar ejes ortogonales
ax.quiver(0, 0, 0, r, 0, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, r, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, -r, 0, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, -r, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 0, z, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)

# Agregar etiquetas a los ejes
ax.text(r, 0, 0, 'X', fontsize=12)
ax.text(0, r, 0, 'Y', fontsize=12)
ax.text(-r, 0, 0, '-X', fontsize=12)
ax.text(0, -r, 0, '-Y', fontsize=12)
if (z > 0):
    ax.text(0, 0, h, 'Z', fontsize=12)
else:
    ax.text(0, 0, h, '-Z', fontsize=12)

ax.quiver(0, 0, 0, x, y, z, color='green', linewidth=1.5, arrow_length_ratio=0.1)

# Línea 1
x1_start, y1_start, z1_start = 0, 0, 0
x1_end, y1_end, z1_end = x, y, 0
ax.plot([x1_start, x1_end], [y1_start, y1_end], [z1_start, z1_end], linestyle='dotted', color='black')
ax.text(x1_end/2, y1_end/2, z1_end, 'r', fontsize=12)

# Línea 2
x2_start, y2_start, z2_start = x1_end, y1_end, z1_end
x2_end, y2_end, z2_end = x, y, z
ax.plot([x2_start, x2_end], [y2_start, y2_end], [z2_start, z2_end], linestyle='dotted', color='black')
ax.text(x2_end, y2_end, z2_end/2, 'h', fontsize=12)

# Línea 3
x3_start, y3_start, z3_start = 0, 0, z
x3_end, y3_end, z3_end = x, y, z
ax.plot([x3_start, x3_end], [y3_start, y3_end], [z3_start, z3_end], linestyle='dotted', color='black')

# ----------    Curvas de los angulos   ----------

# ->    Curva con respecto al eje x (ángulo θ)
# generacion de todos los valores de x
y_v = np.linspace(0, (0.5 * y * x)/np.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2)), 1000) 

# formulas
if (y != 0):
    X = np.sqrt((pow(x, 2)/4) - pow(y_v, 2) * ((pow(y, 2) + pow(z, 2))/pow(y, 2)))
else:
    X = np.zeros((1000))
Y = np.absolute(y_v)
Z = 0
ax.plot(X, Y, Z, color = "black", label = 'θ')
ax.text(X[500], Y[500], 0, 'θ = ' + str(round(np.rad2deg(theta), 2)) + '°', style='italic', fontweight='bold', color = "black", fontsize=12)

# Configurar gráficos
ax.set_xlabel('Posición_X')
ax.set_ylabel('Posición_Y')
ax.set_zlabel('Posición_Z')
ax.set_title('Coordenadas Cilíndricas')

# Mostrar gráfico
plt.tight_layout()
plt.show()
