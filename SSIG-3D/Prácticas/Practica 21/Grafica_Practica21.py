import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
import numpy as np

#*************************** Clase de Gauss ***************************************************************************************************************************#
class Movi_Circular(FigureCanvas):
    #------------------ Función Inicial---------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Movimiento Circular de muestra -----------------------------------------------------------------------------------------------------------
    def graficar_muestra(self):    

        # Parámetros
        r = 1.0  # Radio de la trayectoria
        mass = 1.0  # Masa del objeto
        num_points = 250  # Número de puntos en la trayectoria
        interval = 0.01  # Intervalo de tiempo entre puntos
        t = np.linspace(0, 2*np.pi, num_points)  # Parámetro t para generar la trayectoria

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        # Trayectoria en coordenadas cartesianas
        x = r * np.cos(t)
        y = r * np.sin(t)
        z = np.zeros_like(t)

        # Vectores de velocidad tangenciales
        vel_x = -r * np.sin(t)
        vel_y = r * np.cos(t)
        vel_z = np.zeros_like(t)

        # Vectores de fuerza centrífuga
        f_cent_x = -((mass / (r*r)) * (vel_x**2 + vel_y**2)) * np.cos(t)
        f_cent_y = -((mass / (r*r)) * (vel_x**2 + vel_y**2)) * np.sin(t)
        f_cent_z = np.zeros_like(t)

        self.ax.set_box_aspect([1, 1, 1])  # Aspecto cuadrado para la caja
        self.ax.set_xlim(-1.5*r, 1.5*r)
        self.ax.set_ylim(-1.5*r, 1.5*r)
        self.ax.set_zlim(-1.5*r, 1.5*r)
        plt.suptitle('Movimiento Circular Uniforme')

        # Línea de la trayectoria
        line, = self.ax.plot([], [], [], color='black', linestyle='--')

        # Actualizar la animación en cada frame
        def update(frame):
            self.ax.cla()  # Borrar el frame anterior
            self.ax.set_xlabel('Posición_X')
            self.ax.set_ylabel('Posición_Y')
            self.ax.set_zlabel('Posición_Z')
            self.ax.set_box_aspect([1, 1, 1])  # Aspecto cuadrado para la caja
            self.ax.quiver(x[frame], y[frame], z[frame], vel_x[frame], vel_y[frame], vel_z[frame], color='red', label=' -> Vector de velocidad')
            self.ax.quiver(x[frame], y[frame], z[frame], f_cent_x[frame], f_cent_y[frame], f_cent_z[frame], color='blue', label=' -> Fuerza centrípeta')
            self.ax.set_xlim(-1.5*r, 1.5*r)
            self.ax.set_ylim(-1.5*r, 1.5*r)
            self.ax.set_zlim(-1.5*r, 1.5*r)
            # Subtítulos en LaTeX
            self.ax.text2D(0.05, 0.95, r'$\vec{r}(t) = r(\cos(t), \sin(t))$', transform=self.ax.transAxes, fontsize=10)
            self.ax.text2D(0.05, 0.90, r'$\vec{v}(t) = v(t)(-\sin(t), \cos(t))$', transform=self.ax.transAxes, fontsize=10)
            self.ax.text2D(0.05, 0.85, r'$\vec{F}_c = \frac{m \cdot v^2}{r^2}(-\cos(t), -\sin(t))$', transform=self.ax.transAxes, fontsize=10)
            plt.legend(loc = 8, ncols = 2, draggable = True)    # Muestra las etiquetas

            line.set_data(x[:frame], y[:frame])
            line.set_3d_properties(z[:frame])

            self.ax.plot(x[:frame], y[:frame], z[:frame], color='black')

        # Generar la animación
        self.ani = FuncAnimation(self.fig, update, frames=num_points, interval=interval*1000)
        plt.tight_layout()
        
    #------------ Grafica de Movimiento Circular de muestra (FIN) ----------------------------------------------------------------------------------------------------

    #------------ Grafica de Movimiento Circular ---------------------------------------------------------------------------------------------------------------------
    def graficar_circular(self, r, mass):   

        # Parámetros
        num_points = 250  # Número de puntos en la trayectoria
        interval = 0.01  # Intervalo de tiempo entre puntos
        t = np.linspace(0, 2*np.pi, num_points)  # Parámetro t para generar la trayectoria

        # Trayectoria en coordenadas cartesianas
        x = r * np.cos(t)
        y = r * np.sin(t)
        z = np.zeros_like(t)

        # Vectores de velocidad tangenciales
        vel_x = -r * np.sin(t)
        vel_y = r * np.cos(t)
        vel_z = np.zeros_like(t)

        # Vectores de fuerza centrífuga
        f_cent_x = -((mass / (r*r)) * (vel_x**2 + vel_y**2)) * np.cos(t)
        f_cent_y = -((mass / (r*r)) * (vel_x**2 + vel_y**2)) * np.sin(t)
        f_cent_z = np.zeros_like(t)

        self.ax.set_box_aspect([1, 1, 1])  # Aspecto cuadrado para la caja
        self.ax.set_xlim(-1.5*r, 1.5*r)
        self.ax.set_ylim(-1.5*r, 1.5*r)
        self.ax.set_zlim(-1.5*r, 1.5*r)
        self.ax.set_xlabel('Posición_X')
        self.ax.set_ylabel('Posición_Y')
        self.ax.set_zlabel('Posición_Z')
        plt.suptitle('Movimiento Circular Uniforme')

        # Línea de la trayectoria
        line, = self.ax.plot([], [], [], color='black', linestyle='--')

        # Actualizar la animación en cada frame
        def update(frame):
            self.ax.cla()  # Borrar el frame anterior
            self.ax.set_box_aspect([1, 1, 1])  # Aspecto cuadrado para la caja
            self.ax.quiver(x[frame], y[frame], z[frame], vel_x[frame], vel_y[frame], vel_z[frame], color='red', label=' -> Vector de velocidad')
            self.ax.quiver(x[frame], y[frame], z[frame], f_cent_x[frame], f_cent_y[frame], f_cent_z[frame], color='blue', label=' -> Fuerza centrípeta')
            self.ax.set_xlim(-1.5*r, 1.5*r)
            self.ax.set_ylim(-1.5*r, 1.5*r)
            self.ax.set_zlim(-1.5*r, 1.5*r)
            # Subtítulos en LaTeX
            self.ax.text2D(0.05, 0.95, r'$\vec{r}(t) = r(\cos(t), \sin(t))$', transform=self.ax.transAxes, fontsize=10)
            self.ax.text2D(0.05, 0.90, r'$\vec{v}(t) = v(t)(-\sin(t), \cos(t))$', transform=self.ax.transAxes, fontsize=10)
            self.ax.text2D(0.05, 0.85, r'$\vec{F}_c = \frac{m \cdot v^2}{r^2}(-\cos(t), -\sin(t))$', transform=self.ax.transAxes, fontsize=10)
            plt.legend(loc = 8, ncols = 2, draggable = True)    # Muestra las etiquetas

            line.set_data(x[:frame], y[:frame])
            line.set_3d_properties(z[:frame])

            self.ax.plot(x[:frame], y[:frame], z[:frame], color='black')

        # Generar la animación
        self.ani = FuncAnimation(self.fig, update, frames=num_points, interval=interval*1000)
        plt.tight_layout()
        
    #------------ Grafica de Movimiento Circular (FIN) -----------------------------------------------------------------------------------------------------------------

    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------------------------------------------------------------------------

#*************************** Clase de Movimiento Circular (FIN) *******************************************************************************************************#