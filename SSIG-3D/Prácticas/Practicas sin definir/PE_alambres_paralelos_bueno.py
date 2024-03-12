import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Definir los valores de rho y phi
rho_values = np.linspace(0, 1, 200)
phi_values = np.linspace(0, 2*np.pi, 200)

# Definir las coordenadas de los puntos rojo y azul
a = 0.1
k = 2 # Factor para incrementar los ejes
x_red = -a
y_red = 0.0
x_blue = a
y_blue = 0.0

# Definir los parámetros de la función
lambda_ = 5.0e-8    #[C/m]
epsilon =  8.85e-12 # [C^2/N m^2]

# Calcular y dibujar las líneas de campo eléctrico
x_values = []
y_values = []
result_values = []
for rho in rho_values:
    for phi in phi_values:
        numerator = a**2 + rho**2 + 2*a*rho*np.cos(phi)
        denominator = a**2 + rho**2 - 2*a*rho*np.cos(phi)
        result = lambda_ / (4*np.pi*epsilon) * np.log(numerator / denominator)
        x = rho * np.cos(phi)
        y = rho * np.sin(phi)
        x_values.append(x)
        y_values.append(y)
        result_values.append(result)

# Crear una cuadrícula cartesiana regular
xi = np.linspace(min(x_values), max(x_values), 500)
yi = np.linspace(min(y_values), max(y_values), 500)
xi, yi = np.meshgrid(xi, yi)

# Interpolar los datos en la cuadrícula
zi = griddata((x_values, y_values), result_values, (xi, yi), method='cubic')

# Dibujar el mapa de colores
plt.pcolormesh(xi, yi, zi, cmap='hot')
# Definir los límites de los ejes
plt.xlim(-k*a, k*a)  # Cambia los números según tus necesidades
plt.ylim(-k*a, k*a)  # Cambia los números según tus necesidades
#plt.axis('equal')

# Dibujar las líneas de equipotencial
contour_values = np.linspace(np.min(result_values), np.max(result_values), 19)  # 9 contornos incluyen 4 a cada lado y 1 en el medio
contours = plt.contour(xi, yi, zi, contour_values, colors='black')
plt.clabel(contours, inline=True, fontsize=8)

# Dibujar los puntos rojo y azul
plt.scatter(x_red, y_red, color='blue')
plt.scatter(x_blue, y_blue, color='red')

# Agregar una barra de colores
cbar = plt.colorbar()
cbar.set_label('Potencial')

# ...
# Mostrar el gráfico
plt.title(r'Potencial electrostático producido por dos líneas de carga opuestas: $\frac{\lambda}{4\pi\epsilon}\ln\left(\frac{a^{2} + \rho^{2}  + 2a\rho\cos(\phi)}{a^{2} + \rho^{2}  - 2a\rho\cos(\phi)}\right)$', fontsize=12)

# Agregar las etiquetas a los ejes
plt.xlabel('[m]')
plt.ylabel('[m]')

# Mostrar el gráfico
plt.show()
