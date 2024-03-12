# probando la (Práctica 4: Tiro parabólico en una sola posición en el tiempo)

import matplotlib.pyplot as plt ## Creación de gráficas
from mpl_toolkits import mplot3d

# Insertando los valores
x0 = float(input('Posicion inicial en x [m]: '))
y0 = float(input('Posicion inicial en y [m]: '))
z0 = float(input('Posicion inicial en z [m]: '))
V0x = float(input('Velocidad inicial en x [m/s]: '))
V0y = float(input('Velocidad inicial en y [m/s]: '))
V0z = float(input('Velocidad inicial en z [m/s]: '))
tiempo = int(input('Tiempo en el que se desea observar[s]: '))

gravedad = 9.81

posX = V0x*float(tiempo) + x0
posY = V0y*float(tiempo) + y0
posZ = -1/2*gravedad*float(pow(tiempo, 2)) + V0z*float(tiempo) + z0

velX = V0x
velY = V0y
velZ = -gravedad*(tiempo) + V0z

fig = plt.figure()
ax = plt.axes(projection="3d")

ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Inserta el nombre al eje Y
ax.set_zlabel("PosiciónZ [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})     # Inserta el nombre al eje Z

ax.plot((posX, 0), (0, 0), (0, 0), color = "orange", label='X(+)')
ax.plot((0, -posX), (0, 0), (0, 0), color = "red", label='X(-)')
ax.plot((0, 0), (posY, 0), (0, 0), color = "green", label='Y(+)')
ax.plot((0, 0), (0, -posY), (0, 0), color = "blue", label='Y(-)')
ax.plot((0, 0), (0, 0), (posZ, 0), color = "yellow", label='Z(+)')
ax.plot((0, 0), (0, 0), (0, -posZ), color = "brown", label='Z(-)')

ax.plot(posX, posY, posZ, marker='o') 
ax.quiver(0, 0, 0, posX, posY, posZ, arrow_length_ratio=0.1)    # Vector Posición
ax.quiver(posX, posY, posZ, velX, velY, velZ, arrow_length_ratio=0.1)   # Vector de velocidad

plt.legend()
plt.show()
