# Archivo con el proceso de graficación y animaciones. Practica 15

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
import numpy as np

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Tiro_Parabolico(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica Tiro --------------------------------------------------
    def graficarTiroPar(self, Xo, Yo, Zo, vox, voy, voz):    # Se piden las variables de otra clase para poder trabajarlos.

        plt.suptitle("Tiro Parabólico")  
        self.ax.set_xlabel("Posición_X [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        # Definimos los parámetros del tiro parabólico
        g = 9.81  # aceleración debido a la gravedad

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

        tmax = (2 * voz) / g  # Calcula el tiempo máximo
        num_frames = 300  # Número de frames para la animación
        time_interval = tmax / num_frames  # Calcula el intervalo de tiempo entre cada frame

        def update(frame):
            # Borramos los datos anteriores
            self.ax.clear()
            
            # Añadimos la trayectoria hasta el tiempo actual
            current_time = frame * time_interval
            t = np.linspace(0, current_time, 100)
            r = np.array([r_vec(ti) for ti in t])
            self.ax.plot(r[:,0], r[:,1], r[:,2], 'b')
            
        # Calcular las posiciones finales xf y yf
            xf = vox * tmax
            yf = voy * tmax
            zf = voz * tmax

            # Definimos los límites del gráfico
            max_range = np.sqrt(xf*xf + yf*yf + zf+zf)
            self.ax.set_xlim([0, max_range])
            self.ax.set_ylim([0, max_range])
            self.ax.set_zlim([0, max_range])

        # Añadimos el plano XY en color 10
            X, Y = np.meshgrid(np.linspace(0, max_range, 2), np.linspace(0, max_range, 2))
            Z = np.zeros_like(X)
            self.ax.plot_surface(X, Y, Z, color='C1', alpha=0.3)

        # Añadimos el punto más alto en color rojo
            t_max_altura = voz / g
            X_max = vox * t_max_altura
            Y_max = voy * t_max_altura
            Z_max = -0.5 * g * t_max_altura**2 + voz * t_max_altura
            self.ax.scatter(X_max, Y_max, Z_max, color='r', marker='o')
            self.ax.text(X_max, Y_max, Z_max, f'altura_max = ({X_max:.2f}, {Y_max:.2f}, {Z_max:.2f})', color = 'blue')

            # Dibujar la línea roja en el plano XY
            self.ax.plot([Xo, xf], [Yo, yf], [0, 0], color='red')

            # Añadir etiqueta con la distancia de impacto
            d_impacto = np.sqrt(pow(xf,2) + pow(yf,2) + pow(zf,2))
            self.ax.text(xf / 4, yf / 4, 0, f'd_impacto = {d_impacto:.2f}', color='red')


            # Añadimos una etiqueta con el tiempo actual
            self.ax.text2D(0.05, 0.95, f'Tiempo: {current_time:.2f} s', transform=self.ax.transAxes)

            return self.ax

        self.ani = FuncAnimation(self.fig, update, frames=num_frames, interval=time_interval*1000, blit=False, repeat=False)
        plt.tight_layout()

    #------------ Función para borrar la gráfica ---------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        plt.clf()

    #------------ Función cerrar ventana -----------------------------------------
    def cerrarGraf(self):
	    plt.close(self.fig)