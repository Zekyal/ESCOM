# Archivo con el proceso de graficación y animaciones. Practica 02

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
    def graficarTiroParabolico(self, X, Y, Z, velX, velY, velZ, time0, usuario):    # Se piden las variables de otra clase para poder trabajarlos.
        self.ax.set_title("Hecho por: " + usuario, loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Tiro Parabólico con Vectores de Velocidad")  
        self.ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("PosiciónZ [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})

        self.ax.plot((max(X)+100, 0), (0, 0), (0, 0), color = "orange", label='X(+)')
        self.ax.plot((0, -max(X)-100), (0, 0), (0, 0), color = "red", label='X(-)')
        self.ax.plot((0, 0), (max(Y)+100, 0), (0, 0), color = "green", label='Y(+)')
        self.ax.plot((0, 0), (0, -max(Y)-100), (0, 0), color = "blue", label='Y(-)')
        self.ax.plot((0, 0), (0, 0), (max(Z)+100, 0), color = "yellow", label='Z(+)')
        self.ax.plot((0, 0), (0, 0), (0, -max(Z)-100), color = "brown", label='Z(-)')

        line, = self.ax.plot(0, 0, 0, marker='o', label='Tiro Parabólico', color='black') 
        #self.ax.quiver(X, Y, Z, velX, velY, velZ, color='coral', label='Vector Velocidad', arrow_length_ratio=0.1) # Graficamos los vectores de velocidad
        # Otra manera de dibujar los vectores
        for i in range(0, int(len(X) - 1), 10):
            Q = self.ax.quiver(X[i], Y[i], Z[i], velX[i], velY[i], velZ[i], color='coral') # Graficamos los vectores de velocidad

        Q.set_label("Vector Velocidad")
        plt.legend()    # Muestra las etiquetas

        def animation(i):     # Función para realizar los frames de la animación

            line.set_data(X[:i], Y[:i])
            line.set_3d_properties(Z[:i])

            return line,

        anim = FuncAnimation(self.fig, func = animation, interval=1, frames=time0*10+1, repeat=False)
        self.fig.canvas.draw()        
        self.fig.canvas.flush_events()
        anim.save('Grafica\Tiro Parabolico.gif')
    #------------ Grafica de Tiro parabólico (FIN) -------------------------------

    #------------ Función para borrar la gráfica ---------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        plt.clf()

    #------------ Función para borrar la gráfica (FIN) ---------------------------