# Archivo con el proceso de graficación y animaciones. Practica 04

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Componentes(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Tiro parabólico -------------------------------------
    def graficarVectorComp(self, i, j, k, directoj):    # Se piden las variables de otra clase para poder trabajarlos.
        # Titulo de la grafica
        plt.suptitle("Grafica de un Vector")
        # Nombres de los ejes
        self.ax.set_xlabel("PosiciónX", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("PosiciónZ", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        # Definicion de los ejes x, y, z que se marcaran para definir la grafica
        if (i >= 0 ):
            self.ax.plot((0, 1.25*i), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.text(1.25*i, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((1.25*i, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*i, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        
        if (j >= 0 ):
            self.ax.plot((0, 0), (0, 1.25*j), (0, 0), color = "green", label='Y')
            self.ax.text(0, 1.25*j, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (1.25*j, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*j, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)

        if (k >= 0):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*k), color = "slateblue", label='Z')
            self.ax.text(0, 0, 1.25*k, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (0, 0), (1.25*k, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*k, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)

        # Ejes i, j y k traslapados
        self.ax.plot((0, i), (j, j), (0, 0), color = "cyan", linestyle = "dashed", label='i')
        self.ax.plot((i, i), (0, j), (0, 0), color = "darkviolet", linestyle = "dashed", label='j')
        self.ax.plot((i, i), (j, j), (0, k), color = "black", linestyle = "dashed", label='k')

        # Ejes i, j y k en el origen
        #self.ax.plot((0, i), (0, 0), (0, 0), color = "cyan", linestyle = "dashed")
        #self.ax.plot((0, 0), (0, j), (0, 0), color = "darkviolet", linestyle = "dashed")
        #self.ax.plot((0, 0), (0, 0), (0, k), color = "black", linestyle = "dashed")
        self.ax.quiver(0, 0, 0, i, 0, 0, arrow_length_ratio=0.1, color = "cyan")
        self.ax.quiver(0, 0, 0, 0, j, 0, arrow_length_ratio=0.1, color = "darkviolet")
        self.ax.quiver(0, 0, 0, 0, 0, k, arrow_length_ratio=0.1, color = "black")

        # r (Solo sirve para darle el efecto de librito)
        self.ax.plot((0, i), (0, j), (0, 0), color = "red", linestyle = "dashed")
        self.ax.plot((0, i), (0, j), (k, k), color = "red", linestyle = "dashed")

        # Vector
        self.ax.quiver(0, 0, 0, i, j, k, arrow_length_ratio=0.1, label='Vector')

        plt.legend(ncol = 4, loc = 8, draggable = True)
        plt.tight_layout()

        plt.savefig(directoj + "/VectorComponentes.jpg")
    #------------ Grafica de Tiro parabólico (FIN) -------------------------------

    #------------ Función para borrar la gráfica ---------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        plt.clf()

    #------------ Función para borrar la gráfica (FIN) ---------------------------