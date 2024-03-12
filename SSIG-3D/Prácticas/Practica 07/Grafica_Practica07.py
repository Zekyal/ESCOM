## Archivo para el módulo de Cosenos Directores
from PyQt5 import QtWidgets

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d
import numpy as np

#*************************** Clase de Tiro Parabólico **********************************************************************************************************
class Cosenos_directores(FigureCanvas):
    #------------------ Función Inicial-----------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica del Vector ------------------------------------------------------------------
    def graficar_vector_cos(self, magnitud, rx, ry, rz):    
        self.ax.set_title("Vector hecho a partir de sus Cosenos Directores y su Magnitud", loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("PosiciónZ [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})

        # ----------   Ejes de la grafica    ----------
        self.ax.plot((magnitud, 0), (0, 0), (0, 0), color = "orange", label='X(+)')
        self.ax.plot((0, -magnitud), (0, 0), (0, 0), color = "red", label='X(-)')
        self.ax.plot((0, 0), (magnitud, 0), (0, 0), color = "green", label='Y(+)')
        self.ax.plot((0, 0), (0, -magnitud), (0, 0), color = "blue", label='Y(-)')
        self.ax.plot((0, 0), (0, 0), (magnitud, 0), color = "slateblue", label='Z(+)')
        self.ax.plot((0, 0), (0, 0), (0, -magnitud), color = "brown", label='Z(-)')


        # ----------    Vector  ----------
        self.ax.quiver(0, 0, 0, rx, ry, rz, arrow_length_ratio=0.1, label='Vector')
        # nombre del vector
        self.ax.text(rx, ry, rz, 'vector', style='italic', fontweight='bold', color = plt.rcParams['axes.prop_cycle'].by_key()['color'][0])


        # ----------    Componentes i, j y k   ----------
        self.ax.quiver(0, 0, 0, rx, 0, 0, arrow_length_ratio=0.1, color = "gray")
        self.ax.quiver(0, 0, 0, 0, ry, 0, arrow_length_ratio=0.1, color = "darkviolet")
        self.ax.quiver(0, 0, 0, 0, 0, rz, arrow_length_ratio=0.1, color = "black")
        # nombres de los ejes
        self.ax.text(3*rx/4, 0, 0, 'i', style='italic', fontweight='bold', color = "gray")
        self.ax.text(0, 3*ry/4, 0, 'j', style='italic', fontweight='bold', color = "darkviolet")
        self.ax.text(0, 0, 3*rz/4, 'k', style='italic', fontweight='bold', color = "black")


        # ----------    Componentes i, j y k traslapados   ----------
        self.ax.plot((0, rx), (ry, ry), (0, 0), color = "cyan", linestyle = "dotted", label='i')
        self.ax.plot((rx, rx), (0, ry), (0, 0), color = "darkviolet", linestyle = "dotted", label='j')
        self.ax.plot((rx, rx), (ry, ry), (0, rz), color = "black", linestyle = "dotted", label='k')


        # ----------    Efecto del "librito"    ----------
        self.ax.plot((0, rx), (0, ry), (0, 0), color = "red", linestyle = "dotted")
        self.ax.plot((0, rx), (0, ry), (rz, rz), color = "red", linestyle = "dotted")


        # ----------    Curvas de los angulos   ----------
        sgnRx = rx/np.absolute(rx)
        sgnRy = ry/np.absolute(ry)
        sgnRz = rz/np.absolute(rz)

        # ->    Curva con respecto al eje z (angulo α)
        # generacion de todos los valores de x 
        x = np.linspace(0, (0.5 * rx * rz)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 100) 

        # formulas
        X = np.absolute(x) * sgnRx
        Y = np.absolute((ry / rx) * x) * sgnRy
        Z = sgnRz * np.sqrt((pow(rz, 2)/4) - pow(x, 2) * ((pow(rx, 2) + pow(ry, 2))/pow(rx, 2)))
        self.ax.plot(X, Y, Z, color = "green")

        # ->    Curva con respecto al eje y (angulo ɣ)
        # generacion de todos los valores de y
        z = np.linspace(0, (0.5 * rz * ry)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 100)

        # formulas
        X = np.absolute((rx / rz) * z) * sgnRx
        Y = sgnRy * np.sqrt((pow(ry, 2)/4) - pow(z, 2) * ((pow(rx, 2) + pow(rz, 2))/pow(rz, 2)))
        Z = np.absolute(z) * sgnRz 
        self.ax.plot(X, Y, Z, color = "blue")

        # ->    Curva con respecto al eje x (angulo β)
        # generacion de todos los valores de x
        y = np.linspace(0, (0.5 * ry * rx)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 100) 

        # formulas
        X = sgnRx * np.sqrt((pow(rx, 2)/4) - pow(y, 2) * ((pow(ry, 2) + pow(rz, 2))/pow(ry, 2)))
        Y = np.absolute(y) * sgnRy
        Z = np.absolute((rz / ry) * y) * sgnRz
        self.ax.plot(X, Y, Z, color = "red")


        plt.legend(loc = 'lower center', bbox_to_anchor=(0.3, -0.1, 0.5, 0.5), ncols = 5)
        plt.tight_layout()
    #------------ Grafica de vector (FIN) ----------------------------------------

    def guardar_graf(self, direccion):
        plt.savefig(direccion + '/VectorCosenos.jpg')

    #------------ Función para borrar la gráfica -----------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        plt.clf()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------
