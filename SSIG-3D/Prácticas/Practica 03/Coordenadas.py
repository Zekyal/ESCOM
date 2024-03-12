# Archivo con el proceso de graficación.

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
#from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
from mpl_toolkits import mplot3d
import numpy as np

class Canvas_Grafica(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Cartesianas -> Esféricas ----------------------------------
    def graficarC(self, rx, ry, rz, phi):    # Se piden las variables de otra clase para poder trabajarlos.

        self.ax.set_title('Coordenadas Cartesianas -> Coordenadas Esféricas', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.xaxis.set_label_text('x', color = 'b')
        self.ax.yaxis.set_label_text('y', color = 'b')
        self.ax.zaxis.set_label_text('z', color = 'b')

        self.ax.grid()  # Asigna la cudarícula

        self.ax.plot((2, 0), (0, 0), (0, 0), color = "orange", label='X(+)')
        self.ax.plot((0, -2), (0, 0), (0, 0), color = "red", label='X(-)')
        self.ax.plot((0, 0), (2, 0), (0, 0), color = "green", label='Y(+)')
        self.ax.plot((0, 0), (0, -2), (0, 0), color = "blue", label='Y(-)')
        self.ax.plot((0, 0), (0, 0), (2, 0), color = "yellow", label='Z(+)')
        self.ax.plot((0, 0), (0, 0), (0, -2), color = "brown", label='Z(-)')

        self.ax.plot((rx, rx), (0, ry), (0, 0), color = "red", linestyle = "dashed")
        self.ax.plot((0, rx), (ry, ry), (0, 0), color = "red", linestyle = "dashed")
        self.ax.plot((rx, rx), (ry, ry), (0, rz), color = "red", linestyle = "dashed")
        self.ax.plot((0, rx), (0, rx*np.tan(phi)), (0, 0), color = "red", linestyle = "dashed")
        self.ax.plot((0, rx), (0, rx*np.tan(phi)), (rz, rz), color = "red", linestyle = "dashed")

        self.ax.quiver(0, 0, 0, rx, ry, rz, arrow_length_ratio=0.1, label='Coordenadas')
        plt.legend() # Muestra las etiquetas

        self.fig.tight_layout()
    #------------ Grafica de Cartesianas -> Esféricas (FIN) -------------------------------------

    def graficarE(self, rx, ry, rz, phi):    # Se piden las variables de otra clase para poder trabajarlos.

        self.ax.set_title('Coordenadas Esféricas -> Coordenadas Cartesianas', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.xaxis.set_label_text('x', color = 'b')
        self.ax.yaxis.set_label_text('y', color = 'b')
        self.ax.zaxis.set_label_text('z', color = 'b')

        self.ax.grid()  # Asigna la cudarícula

        self.ax.plot((2, 0), (0, 0), (0, 0), color = "orange", label='X(+)')
        self.ax.plot((0, -2), (0, 0), (0, 0), color = "red", label='X(-)')
        self.ax.plot((0, 0), (2, 0), (0, 0), color = "green", label='Y(+)')
        self.ax.plot((0, 0), (0, -2), (0, 0), color = "blue", label='Y(-)')
        self.ax.plot((0, 0), (0, 0), (2, 0), color = "yellow", label='Z(+)')
        self.ax.plot((0, 0), (0, 0), (0, -2), color = "brown", label='Z(-)')

        self.ax.plot((rx, rx), (0, ry), (0, 0), color = "red", linestyle = "dashed")
        self.ax.plot((0, rx), (ry, ry), (0, 0), color = "red", linestyle = "dashed")
        self.ax.plot((rx, rx), (ry, ry), (0, rz), color = "red", linestyle = "dashed")
        self.ax.plot((0, rx), (0, rx*np.tan(phi)), (0, 0), color = "red", linestyle = "dashed")
        self.ax.plot((0, rx), (0, rx*np.tan(phi)), (rz, rz), color = "red", linestyle = "dashed")

        self.ax.quiver(0, 0, 0, rx, ry, rz, arrow_length_ratio=0.1, label='Coordenadas')
        plt.legend() # Muestra las etiquetas

        self.fig.tight_layout()
    #------------ Grafica de Cartesianas -> Esféricas (FIN) -------------------------------------

    #------------ Función para borrar la gráfica ---------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        plt.clf()

    #------------ Función para borrar la gráfica (FIN) ---------------------------