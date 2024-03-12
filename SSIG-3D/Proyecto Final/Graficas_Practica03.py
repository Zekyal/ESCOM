# Archivo con el proceso de graficación. Practica03.

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
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

        self.ax.set_title('Coordenadas Cartesianas -> Coordenadas Esféricas', loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")
        
        #magnitud = np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2))

        # Definicion de los ejes x, y, z que se marcaran para definir la grafica
        if (rx >= 0 ):
            self.ax.plot((0, 1.25*rx), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.text(1.25*rx, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((1.25*rx, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*rx, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        
        if (ry >= 0 ):
            self.ax.plot((0, 0), (0, 1.25*ry), (0, 0), color = "green", label='Y')
            self.ax.text(0, 1.25*ry, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (1.25*ry, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*ry, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)

        if (rz >= 0):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*rz), color = "slateblue", label='Z')
            self.ax.text(0, 0, 1.25*rz, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (0, 0), (1.25*rz, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*rz, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)

        self.ax.plot((rx, rx), (0, ry), (0, 0), color = "black", linestyle = "dotted")
        self.ax.plot((0, rx), (ry, ry), (0, 0), color = "black", linestyle = "dotted")
        self.ax.plot((rx, rx), (ry, ry), (0, rz), color = "black", linestyle = "dotted")
        self.ax.plot((0, rx), (0, rx*np.tan(phi)), (0, 0), color = "black", linestyle = "dotted")
        self.ax.plot((0, rx), (0, rx*np.tan(phi)), (rz, rz), color = "black", linestyle = "dotted")

        self.ax.quiver(0, 0, 0, rx, ry, rz, arrow_length_ratio=0.1)
        self.ax.text(rx, ry, rz, 'Vector', style='italic', fontweight='bold', color = plt.rcParams['axes.prop_cycle'].by_key()['color'][0])
        plt.legend(loc = 'lower center', bbox_to_anchor=(0.3, -0.1, 0.5, 0.5), ncols = 3, draggable = True) # Muestra las etiquetas

        plt.tight_layout()
    #------------ Grafica de Cartesianas -> Esféricas (FIN) -------------------------------------

    #------------ Grafica de Esféricas -> Cartesianas  ----------------------------------
    def graficarE(self, rx, ry, rz, phi):    # Se piden las variables de otra clase para poder trabajarlos.

        self.ax.set_title('Coordenadas Esféricas -> Coordenadas Cartesianas', loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")
        
        #magnitud = np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2))

        # Definicion de los ejes x, y, z que se marcaran para definir la grafica
        if (rx >= 0 ):
            self.ax.plot((0, 1.25*rx), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.text(1.25*rx, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((1.25*rx, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*rx, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        
        if (ry >= 0 ):
            self.ax.plot((0, 0), (0, 1.25*ry), (0, 0), color = "green", label='Y')
            self.ax.text(0, 1.25*ry, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (1.25*ry, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*ry, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)

        if (rz >= 0):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*rz), color = "slateblue", label='Z')
            self.ax.text(0, 0, 1.25*rz, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (0, 0), (1.25*rz, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*rz, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)

        self.ax.plot((rx, rx), (0, ry), (0, 0), color = "black", linestyle = "dotted")
        self.ax.plot((0, rx), (ry, ry), (0, 0), color = "black", linestyle = "dotted")
        self.ax.plot((rx, rx), (ry, ry), (0, rz), color = "black", linestyle = "dotted")
        self.ax.plot((0, rx), (0, rx*np.tan(phi)), (0, 0), color = "black", linestyle = "dotted")
        self.ax.plot((0, rx), (0, rx*np.tan(phi)), (rz, rz), color = "black", linestyle = "dotted")

        self.ax.quiver(0, 0, 0, rx, ry, rz, arrow_length_ratio=0.1)
        self.ax.text(rx, ry, rz, 'Vector', style='italic', fontweight='bold', color = plt.rcParams['axes.prop_cycle'].by_key()['color'][0])
        plt.legend(loc = 'lower center', bbox_to_anchor=(0.3, -0.1, 0.5, 0.5), ncols = 3, draggable = True) # Muestra las etiquetas

        plt.tight_layout()
    #------------ Grafica de Esféricas -> Cartesianas (FIN) -------------------------------------

    #------------ Función para borrar la gráfica ---------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        plt.clf()

    #------------ Función para borrar la gráfica (FIN) ---------------------------
    def cerrarGraf(self):
        plt.close(self.fig)