#Este programa calcula la posición final X,Y y Z, dada la distancia que hay de un punto fijo sobre el plano XY y el origen. Considerando 
#valor inicial del las velocidades en sus respectivas coordenadas.


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Definimos los parámetros del tiro parabólico
m = 1  # masa
g = 9.81  # aceleración debido a la gravedad
#Dame la velocidad_inicial_X
vox = 10
#Dame_la_veloidad_incial_Y
voy = 10  
if vox ==0  and voy==0:
    print('la distancia final de impacto es cero y por lo tanto cae sobre si mismo')
    exit(0)

#Dame_la velocidad_inicial_Z
voz = 50.0 
tmax = (2*voz)/g
# (Salida)La distancia final de impacto es: 
dmax = np.sqrt(pow(vox*tmax,2) + pow(voy*tmax,2) + pow(-g*tmax*tmax/2.0 + voz*tmax,2))
#Elige una valor de la distancia final, <= que la distancia final de impacto, pord = es el porcentaje de la distancia de impacto pord = (0,1]
pord = 0.4
if pord ==0:
    print('la distancia final de impacto es cero y por lo tanto cae sobre si mismo')
    exit(0)

dist = pord *dmax  #distancia del origen a un punto en el plano XY
ao = np.sqrt(pow(vox,2) + pow(voy,2))  
tfi = dist/ao  # tiempo final para recorrer la distancia d =  dist
print('tmax, tfi =', tmax, tfi)
#exit(0)
# No se le pide posición inicial, por  default se tiene:
Xo = 0
Yo = 0
Zo = 0

# Definimos las ecuaciones de movimiento
def r_vec(t):
    x = vox * t + Xo
    y = voy * t + Yo
    z = -0.5 * g * t**2 + voz * t + Zo
    return np.array([x, y, z])

def v_vec(t):
    vx = vox
    vy = voy
    vz = -g * t + voz
    return np.array([vx, vy, vz])

# Creamos la figura y el gráfico en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Definimos los límites del gráfico
max_range = 300
ax.set_xlim([0, max_range])
ax.set_ylim([0, max_range])
ax.set_zlim([0, 2*max_range])

#tmax = (2 * voz) / g  # Calcula el tiempo máximo
num_frames = 300  # Número de frames para la animación
time_interval = tfi / num_frames  # Calcula el intervalo de tiempo entre cada frame

def update(frame):
    # Borramos los datos anteriores
    ax.clear()
    
    # Añadimos el plano XY en color 10
    X, Y = np.meshgrid(np.linspace(0, max_range, 2), np.linspace(0, max_range, 2))
    Z = np.zeros_like(X)
    ax.plot_surface(X, Y, Z, color='C1', alpha=0.3)
    
    # Añadimos la trayectoria hasta el tiempo actual
    current_time = frame * time_interval
    t = np.linspace(0, current_time, 100)
    r = np.array([r_vec(ti) for ti in t])
    ax.plot(r[:,0], r[:,1], r[:,2], 'b')
    
# Calcular las posiciones finales xf y yf
    xf = vox * tfi
    yf = voy * tfi
    zf =  -0.5 * g * tfi**2 + voz * tfi

   # Añadimos el punto más alto en color rojo
    t_max_altura = voz / g
    X_max = vox * t_max_altura
    Y_max = voy * t_max_altura
    Z_max = -0.5 * g * t_max_altura**2 + voz * t_max_altura
    ax.scatter(X_max, Y_max, Z_max, color='r', marker='o')
    ax.text(X_max, Y_max, Z_max, f'altura_max = ({X_max:.2f}, {Y_max:.2f}, {Z_max:.2f})', color = 'blue')
    ax.scatter(xf, yf, zf, color='g', marker='o')
    ax.text(xf, yf, zf, f'posición_final = ({xf:.2f}, {yf:.2f}, {zf:.2f})', color = 'blue')


    # Dibujar la línea roja en el plano XY
    ax.plot([Xo, xf], [Yo, yf], [0, 0], color='red')

    # Añadir etiqueta con la distancia de impacto
    d_final = np.sqrt(pow(xf,2) + pow(yf,2) + pow(zf,2))

    ax.text(xf / 4, yf / 4, 0, f'd_final = {d_final:.2f}', color='red')


    # Añadimos una etiqueta con el tiempo actual
    ax.text2D(0.05, 0.95, f'Tiempo: {current_time:.2f} s', transform=ax.transAxes)

    return ax

ani = FuncAnimation(fig, update, frames=num_frames, interval=time_interval*1000, blit=False, repeat=False)

plt.show()
