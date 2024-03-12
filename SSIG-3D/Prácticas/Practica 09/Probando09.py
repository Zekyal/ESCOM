# Aquí haremos todo el programa sin interfaz (Práctica 9: 2da ley de Newton)

import matplotlib.pyplot as plt ## Creación de gráficas
import numpy as np
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas

# Insertando los valores
thetha = float(input('θ [Grados]: '))
Ms = float(input('Coeficiente de fricción Cinética: '))

fig, ax = plt.subplots()

thetha_v = np.deg2rad(thetha)
#Ms = 0.1    ## Agregado por usuairo
l = 50  # Largo 
#m = 20
g = -9.81
Mk = 0.7*Ms
t = 5

x = l*np.cos(thetha_v)
y = l*np.sin(thetha_v)
#w = m*g
#N = m*g*np.cos(thetha)
acx = g*(Mk*np.cos(thetha_v)- np.sin(thetha_v))
thethaO = np.arctan(Ms)

posX = []
posY = []
velX = []
velY = []

plt.axvline(0, color='dimgray') # Dibuja un eje en y
plt.axhline(0, color='dimgray') # Dibuja un eje en x

print("θ = " + str(thetha))
print("θo = " + str(np.degrees(thethaO)))

# Dibujando el triángulo
plt.plot([0, x],[0, y], color="green")
plt.plot([0, -x],[0, -y], color="green")
plt.plot([x, x],[y, -y], color="green")
plt.plot([-x, x],[-y, -y], color="green")
for i in range(0, t, 1):
    posX.append(-(acx*np.cos(thetha_v)*pow(i, 2))/2)
    posY.append(-(acx*np.sin(thetha_v)*pow(i, 2))/2)
    velX.append(-acx*np.cos(thetha_v)*i)
    velY.append(-acx*np.sin(thetha_v)*i)

#ax.quiver(0, 0, -y, x, color="steelblue", label="N")
#ax.quiver(0, 0, x, -x, color="darkblue", label="Wy")
#ax.quiver(0, 0, 0, -w, color="blueviolet", label="W")

line, = plt.plot(0, 0, marker="o", label='Objeto', color ="indigo")    # objeto en movimiento
Q = ax.quiver([0, 0], [0, 0], 0, 10, color= 'blue', units='inches', label='Vector Velocidad')   # Para la creación de flechas
#plt.plot([0],[0], marker="o" ,color="tomato", label = "Objeto")

ax.set_xlim(-x-2, x+2)     
ax.set_ylim(-y-2, y+2)     


plt.grid()
plt.tight_layout()
plt.legend()

def animation(i):     # Función para realizar los frames de la animación
    x_data1 = []
    y_data1 = []
    x_data1.append(posX[i])  # Inserta punto a punto los valores a las listas vacias.
    y_data1.append(posY[i])
    line.set_xdata(x_data1)
    line.set_ydata(y_data1)

    u = float(velX[i])
    v = float(velY[i])
    y = 1
    Q.set_offsets([[x_data1, y_data1]])    # Actualiza los valores de la posición inicial de la quiver.
    Q.set_UVC(u, v, y)        # Actualiza los valores de la posición final de la quiver.

    return line, Q,

if (thetha > np.degrees(thethaO)):
    anim01 = FuncAnimation(fig, animation, interval=1000, frames=len(posX), repeat=True)

plt.show()