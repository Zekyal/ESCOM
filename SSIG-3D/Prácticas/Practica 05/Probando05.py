# probando la (Práctica 5: 1ra Ley de Newton (Ley de Inercia)

import matplotlib.pyplot as plt ## Creación de gráficas
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas

# Insertando los valores
V0x = float(input('Velocidad inicial en x [m/s]: '))
V0y = float(input('Velocidad inicial en y [m/s]: '))
V0z = float(input('Velocidad inicial en z [m/s]: '))
tiempo = int(input('Tiempo [s]: '))

posX = []
posY = []
posZ = []

for i in range (0, tiempo*10+1, 1):
    posX.append(V0x*float(i/10))
    posY.append(V0y*float(i/10))
    posZ.append(V0z*float(i/10))

velX = V0x
velY = V0y
velZ = V0z

fig = plt.figure()
ax = plt.axes(projection="3d")

ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Inserta el nombre al eje Y
ax.set_zlabel("PosiciónZ [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})     # Inserta el nombre al eje Z

if(max(posX) > 0):
    ax.plot((max(posX), 0), (0, 0), (0, 0), color = "orange", label='X(+)')
    ax.plot((0, -max(posX)), (0, 0), (0, 0), color = "red", label='X(-)')
else:
    ax.plot((-min(posX), 0), (0, 0), (0, 0), color = "orange", label='X(+)')
    ax.plot((0, min(posX)), (0, 0), (0, 0), color = "red", label='X(-)')
if(max(posY) > 0): 
    ax.plot((0, 0), (max(posY), 0), (0, 0), color = "green", label='Y(+)')
    ax.plot((0, 0), (0, -max(posY)), (0, 0), color = "blue", label='Y(-)')
else:
    ax.plot((0, 0), (-min(posY), 0), (0, 0), color = "green", label='Y(+)')
    ax.plot((0, 0), (0, min(posY)), (0, 0), color = "blue", label='Y(-)')
if(max(posZ) > 0):
    ax.plot((0, 0), (0, 0), (max(posZ), 0), color = "yellow", label='Z(+)')
    ax.plot((0, 0), (0, 0), (0, -max(posZ)), color = "brown", label='Z(-)')
else:
    ax.plot((0, 0), (0, 0), (-min(posZ), 0), color = "yellow", label='Z(+)')
    ax.plot((0, 0), (0, 0), (0, min(posZ)), color = "brown", label='Z(-)')


line, = ax.plot(posX, posY, posZ, color="crimson", linestyle="--", marker="o") 

for i in range(0, int(len(posX) - 1), 10):
    ax.quiver(posX[i], posY[i], posZ[i], velX, velY, velZ, color="darkgoldenrod")   # Vector de velocidad

def animation(i):     # Función para realizar los frames de la animación

            line.set_data(posX[:i], posY[:i])
            line.set_3d_properties(posZ[:i])

            return line,

anim = FuncAnimation(fig, func = animation, interval=10, frames=len(posX), repeat=True)
fig.canvas.draw()        
fig.canvas.flush_events()
anim.save('Practica05_graf\Ley_Inercia.gif')

plt.legend()
plt.show()
