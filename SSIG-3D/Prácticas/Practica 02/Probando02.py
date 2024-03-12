# Aquí haremos todo el programa sin interfaz (Práctica 2: Tiro parabólico)

# Vox*t + Xo, Voy*t + Yo, -1/2*g*t^2 + Voz*t + Zo
import matplotlib.pyplot as plt ## Creación de gráficas
from mpl_toolkits import mplot3d

# Insertando los valores
x0 = float(input('Posicion inicial en x [m]: '))
y0 = float(input('Posicion inicial en y [m]: '))
z0 = float(input('Posicion inicial en z [m]: '))
V0x = float(input('Velocidad inicial en x [m]: '))
V0y = float(input('Velocidad inicial en y [m]: '))
V0z = float(input('Velocidad inicial en z [m]: '))
tiempo = int(input('Tiempo [s]: '))

gravedad = 9.81

posX = []
posY = []
posZ = []

for t in range(0, tiempo, 1):
    posX.append(V0x*float(t/100) + x0)
    posY.append(V0y*float(t/100) + y0)
    posZ.append(-1/2*gravedad*float(pow(t/100, 2)) + V0z*float(t/100) + z0)
    
#print(posX)
#print('----')
#print(posY)
#print('----')
#print(posZ)

fig = plt.figure()
ax = plt.axes(projection="3d")

ax.plot(posX, posY, posZ, marker='o') 

plt.show()


