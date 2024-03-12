import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Definimos los parámetros del tiro parabólico
#m = 1  # masa
g = 9.81  # aceleración debido a la gravedad
vox = 10.0
voy = 10.0
voz = 50.0
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
max_range = 100
ax.set_xlim([0, max_range])
ax.set_ylim([0, max_range])
ax.set_zlim([0, 2*max_range])

tmax = (2 * voz) / g  # Calcula el tiempo máximo
num_frames = 300  # Número de frames para la animación
time_interval = tmax / num_frames  # Calcula el intervalo de tiempo entre cada frame

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
    xf = vox * tmax
    yf = voy * tmax
    zf = voz * tmax

   # Añadimos el punto más alto en color rojo
    t_max_altura = voz / g
    X_max = vox * t_max_altura
    Y_max = voy * t_max_altura
    Z_max = -0.5 * g * t_max_altura**2 + voz * t_max_altura
    ax.scatter(X_max, Y_max, Z_max, color='r', marker='o')
    ax.text(X_max, Y_max, Z_max, f'altura_max = ({X_max:.2f}, {Y_max:.2f}, {Z_max:.2f})', color = 'blue')

    # Dibujar la línea roja en el plano XY
    ax.plot([Xo, xf], [Yo, yf], [0, 0], color='red')

    # Añadir etiqueta con la distancia de impacto
    d_impacto = np.sqrt(pow(xf,2) + pow(yf,2) + pow(zf,2))
    ax.text(xf / 4, yf / 4, 0, f'd_impacto = {d_impacto:.2f}', color='red')


    # Añadimos una etiqueta con el tiempo actual
    ax.text2D(0.05, 0.95, f'Tiempo: {current_time:.2f} s', transform=ax.transAxes)

    return ax

ani = FuncAnimation(fig, update, frames=num_frames, interval=time_interval*1000, blit=False, repeat=False)

plt.show()
