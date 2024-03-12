# Archivo con el proceso de graficación y animaciones. Practica 02.

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
from mpl_toolkits import mplot3d

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Canvas_grafica(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Tiro parabólico -------------------------------------
    def graficarTiroParabolico(self, X, Y, Z, velX, velY, velZ, time0):    # Se piden las variables de otra clase para poder trabajarlos.
        self.ax.set_title("Tiro Parabólico con Vectores de Velocidad.", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("PosiciónZ [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        max_axis_x = max(X)
        min_axis_x = min(X)
        max_axis_y = max(Y)
        min_axis_y = min(Y)
        max_axis_z = max(Z)
        min_axis_z = min(Z)

        # Definicion de los ejes x, y, z que se marcaran para definir la grafica
        if ((max_axis_x >= 0 ) and (min_axis_x >= 0)):
            self.ax.plot((0, 1.25*max_axis_x), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.text(1.25*max_axis_x, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_x >= 0 ) and (min_axis_x < 0)):
            self.ax.plot((0, 1.25*max_axis_x), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.plot((1.25*min_axis_x, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*max_axis_x, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(1.25*min_axis_x, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((1.25*min_axis_x, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*min_axis_x, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        
        if ((max_axis_y >= 0 ) and (min_axis_y >= 0)):
            self.ax.plot((0, 0), (0, 1.25*max_axis_y), (0, 0), color = "green", label='Y')
            self.ax.text(0, 1.25*max_axis_y, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_y >= 0 ) and (min_axis_y < 0)):
            self.ax.plot((0, 0), (0, 1.25*max_axis_y), (0, 0), color = "green", label='Y')
            self.ax.plot((0, 0), (1.25*min_axis_y, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*max_axis_y, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(0, 1.25*min_axis_y, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (1.25*min_axis_y, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*min_axis_y, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)

        if ((max_axis_z >= 0 ) and (min_axis_z >= 0)):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*max_axis_z), color = "slateblue", label='Z')
            self.ax.text(0, 0, 1.25*max_axis_z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_z >= 0 ) and (min_axis_z < 0)):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*max_axis_z), color = "slateblue", label='Z')
            self.ax.plot((0, 0), (0, 0), (1.25*min_axis_z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*max_axis_z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(0, 0, 1.25*min_axis_z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (0, 0), (1.25*min_axis_z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*min_axis_z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)

        line, = self.ax.plot(0, 0, 0, marker='o', label='Tiro Parabólico', color='black') 
        #self.ax.quiver(X, Y, Z, velX, velY, velZ, color='coral', label='Vector Velocidad', arrow_length_ratio=0.1) # Graficamos los vectores de velocidad
        # Otra manera de dibujar los vectores
        for i in range(0, int(len(X) - 1), 100):
            Q = self.ax.quiver(X[i], Y[i], Z[i], velX[i], velY[i], velZ[i], color='coral') # Graficamos los vectores de velocidad

        Q.set_label("-> Vector Velocidad")
        plt.legend(loc = 'lower center', bbox_to_anchor=(0.3, -0.1, 0.5, 0.5), ncols = 3, draggable = True)    # Muestra las etiquetas
        plt.tight_layout()

        def animation(i):     # Función para realizar los frames de la animación

            line.set_data(X[:i], Y[:i])
            line.set_3d_properties(Z[:i])

            return line,

        anim = FuncAnimation(self.fig, func = animation, interval=0.1, frames=time0*100+1, repeat=False)
        anim.save('Practica02_graf\Tiro Parabolico.gif')
        self.fig.canvas.draw()        
    #------------ Grafica de Tiro parabólico (FIN) -------------------------------

    #------------ Función para borrar la gráfica ---------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        plt.clf()

    #------------ Función para borrar la gráfica (FIN) ---------------------------
    def cerrarGraf(self):
        plt.close(self.fig)