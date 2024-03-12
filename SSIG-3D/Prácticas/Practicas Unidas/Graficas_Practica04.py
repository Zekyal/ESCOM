# Archivo con el proceso de graficación y animaciones. Practica 04

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d
import numpy as np

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Canvas_grafica(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Tiro parabólico -------------------------------------
    def graficarVectorPos(self, X, Y, Z):    # Se piden las variables de otra clase para poder trabajarlos.
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Vector de Posición del Tiro Parabólico")  
        self.ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("PosiciónZ [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        magnitud = np.sqrt(pow(X, 2) + pow(Y, 2) + pow(Z, 2))
        
        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        # Definicion de los ejes x, y, z que se marcaran para definir la grafica
        if (X >= 0 ):
            self.ax.plot((0, 1.25*X), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.text(1.25*X, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((1.25*X, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*X, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        
        if (Y >= 0 ):
            self.ax.plot((0, 0), (0, 1.25*Y), (0, 0), color = "green", label='Y')
            self.ax.text(0, 1.25*Y, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (1.25*Y, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*Y, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)

        if (Z >= 0):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*Z), color = "slateblue", label='Z')
            self.ax.text(0, 0, 1.25*Z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (0, 0), (1.25*Z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*Z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        
        self.ax.plot(X, Y, Z, marker='o', label='Posición') 
        self.ax.quiver(0, 0, 0, X, Y, Z, color='red', label='-> Vector de Posición', arrow_length_ratio=0.1) # Graficamos el vector de Posición
        plt.tight_layout()

        plt.legend(loc = 'lower center', bbox_to_anchor=(0.3, -0.1, 0.5, 0.5), ncols = 3, draggable = True)     # Muestra las etiquetas
        plt.savefig("Practica04_grafs\VectorPosicion.jpg")
    #------------ Grafica de Tiro parabólico (FIN) -------------------------------

    #------------ Función para borrar la gráfica ---------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        plt.clf()

    #------------ Función para borrar la gráfica (FIN) ---------------------------

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Canvas_grafica2(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Tiro parabólico -------------------------------------
    def graficarVectorVel(self, X, Y, Z, velX, velY, velZ):    # Se piden las variables de otra clase para poder trabajarlos.
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Vector de Velocidad del Tiro Parabólico")  
        self.ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("PosiciónZ [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        magnitud = np.sqrt(pow(X, 2) + pow(Y, 2) + pow(Z, 2))
        
         # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        # Definicion de los ejes x, y, z que se marcaran para definir la grafica
        if (X >= 0 ):
            self.ax.plot((0, 1.25*X), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.text(1.25*X, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((1.25*X, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*X, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        
        if (Y >= 0 ):
            self.ax.plot((0, 0), (0, 1.25*Y), (0, 0), color = "green", label='Y')
            self.ax.text(0, 1.25*Y, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (1.25*Y, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*Y, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)

        if (Z >= 0):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*Z), color = "slateblue", label='Z')
            self.ax.text(0, 0, 1.25*Z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (0, 0), (1.25*Z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*Z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        
        self.ax.plot(X, Y, Z, marker='o', label='Posición') 
        self.ax.quiver(X, Y, Z, velX, velY, velZ, color='red', label='Vector de Velocidad', arrow_length_ratio=0.1) # Graficamos eñ vector de velocidad.
        plt.tight_layout()
        
        plt.legend(loc = 'lower center', bbox_to_anchor=(0.3, -0.1, 0.5, 0.5), ncols = 3, draggable = True)    # Muestra las etiquetas
        plt.savefig("Practica04_grafs\VectorVelocidad.jpg")
    #------------ Grafica de Tiro parabólico (FIN) -------------------------------

    #------------ Función para borrar la gráfica ---------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        plt.clf()

    #------------ Función para borrar la gráfica (FIN) ---------------------------