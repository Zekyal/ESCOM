## Archivo para el módulo de Cosenos Directores 2.0. Practica 10

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
    def graficar_vector_cos(self, rx, ry, rz, magnitud):    
        self.ax.set_title("Cosenos Directores y Magnitud de un Vector", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        if rx == 0 or ry ==0 or rz ==0: 

            self.ax.quiver(0,0,0, rx, ry, rz, arrow_length_ratio=0.1, color = 'black' )

            #========================================================================
            # nombre del vector
            self.ax.text(rx, ry, rz, f"({rx}, {ry}, {rz})", style='italic', fontweight='bold', color = 'blue', fontsize=12)

            if rx == 0:
                rx = magnitud
            else:
                rx = rx + 0.2*magnitud*np.sign(rx)
            if ry ==0:
                ry=magnitud
            else:     
                ry = ry + 0.2*magnitud*np.sign(ry)
            if rz ==0:  
                rz = magnitud
            else:     
                rz = rz + 0.2*magnitud*np.sign(rz)

            #dibuja el nombre del eje correspondiente al final de este
            if (rx > 0):
                self.ax.text(1.25*rx, 0, 0, "X", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.text(-0.2*rx, 0, 0, "-X", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.plot((rx, 0), (0, 0), (0, 0), color = "orange", label='X')
                self.ax.plot((0, -0.2*rx), (0, 0), (0, 0), color = "red", label='-X')
            else:
                self.ax.text(-0.2*rx, 0, 0, "X", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.text(1.25*rx, 0, 0, "-X", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.plot((-0.2*rx, 0), (0, 0), (0, 0), color = "orange", label='X')
                self.ax.plot((0, rx), (0, 0), (0, 0), color = "red", label='-X')
            if (ry > 0):
                self.ax.text(0, 1.25*ry, 0, "Y", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.text(0, -0.2*ry, 0, "-Y", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.plot((0, 0), (ry, 0), (0, 0), color = "green", label='Y')
                self.ax.plot((0, 0), (0, -0.2*ry), (0, 0), color = "blue", label='-Y')
            else:
                self.ax.text(0, -0.2*ry, 0, "Y", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.text(0, 1.25*ry, 0, "-Y", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.plot((0, 0), (-0.2*ry, 0), (0, 0), color = "green", label='Y')
                self.ax.plot((0, 0), (0, ry), (0, 0), color = "blue", label='-Y')
            if (rz > 0):
                self.ax.text(0, 0, 1.25*rz, "Z", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.text(0, 0, -0.2*rz, "-Z", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.plot((0, 0), (0, 0), (rz, 0), color = "slateblue", label='Z')
                self.ax.plot((0, 0), (0, 0), (0, -0.2*rz), color = "brown", label='-Z')  
            else:
                self.ax.text(0, 0, -0.2*rz, "Z", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.text(0, 0, 1.25*rz, "-Z", color='teal', style='italic', fontweight='bold', fontsize=12)
                self.ax.plot((0, 0), (0, 0), (-0.2*rz, 0), color = "slateblue", label='Z')
                self.ax.plot((0, 0), (0, 0), (0, rz), color = "brown", label='-Z')  

            plt.legend(ncol = 3, loc = 8, draggable = True)

        else:

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

            self.ax.quiver(0,0,0, rx, ry, rz, arrow_length_ratio=0.1, color = 'black', label="-> Vector")

            #========================================================================
            # nombre del vector
            self.ax.text(rx, ry, rz, f"({rx}, {ry}, {rz})", style='italic', fontweight='bold', color = 'blue', fontsize=12)

            #=============recupera sus valores==========

            # ----------    Componentes i, j y k   ----------
            self.ax.quiver(0, 0, 0, rx, 0, 0, arrow_length_ratio=0.1, color = "black",  alpha = 0.7, linestyle = '--' )
            self.ax.quiver(0, 0, 0, 0, ry, 0, arrow_length_ratio=0.1, color = "black", alpha = 0.7, linestyle = '--' )
            self.ax.quiver(0, 0, 0, 0, 0, rz, arrow_length_ratio=0.1, color = "black", alpha = 0.7, linestyle = '--' )
            # nombres de los ejes
            self.ax.text(rx/2, 0, 0, 'î', style='italic', fontweight='bold', fontsize=12, color = "black")
            self.ax.text(0, ry/2, 0, 'ĵ', style='italic', fontweight='bold', fontsize=12,  color = "black")
            self.ax.text(0, 0, rz/2, 'k̂', style='italic', fontweight='bold', fontsize=12, color = "black")

            # ----------    Componentes i, j y k traslapados   ----------
            self.ax.plot((0, rx), (ry, ry), (0, 0), color = "black", linestyle = "dotted")
            self.ax.plot((rx, rx), (0, ry), (0, 0), color = "black", linestyle = "dotted")
            self.ax.plot((rx, rx), (ry, ry), (0, rz), color = "black", linestyle = "dotted")

            # ----------    Efecto del "librito"    ----------
            self.ax.plot((0, rx), (0, ry), (0, 0), color = "gray", linestyle = "dotted")
            self.ax.plot((0, rx), (0, ry), (rz, rz), color = "green", linestyle = "dotted")

            #-----Efecto planos inclinados ---------
            self.ax.plot((0, rx), (ry, ry), (0, rz), color = "blue", linestyle = "dotted")
            self.ax.plot((rx, rx), (0, ry), (0, rz), color = "red", linestyle = "dotted")

            # ----------    Curvas de los angulos   ----------
            sgnRx = rx/np.absolute(rx)
            sgnRy = ry/np.absolute(ry)
            sgnRz = rz/np.absolute(rz)

            # ->    Curva con respecto al eje x (angulo α)
            # generacion de todos los valores de x
            x = np.linspace(0, (0.5 * ry * rx)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 1000) 

            # formulas
            X = sgnRx * np.sqrt((pow(rx, 2)/4) - pow(x, 2) * ((pow(ry, 2) + pow(rz, 2))/pow(ry, 2)))
            Y = np.absolute(x) * sgnRy
            Z = np.absolute((rz / ry) * x) * sgnRz
            self.ax.plot(X, Y, Z, color = "red", label = 'α')
            self.ax.text(X[500], Y[500], Z[500], 'α', style='italic', fontweight='bold', color = "black", fontsize=12)
            
            # ->    Curva con respecto al eje y (angulo β)
            # generacion de todos los valores de y
            y = np.linspace(0, (0.5 * rz * ry)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 1000)

            # formulas
            X = np.absolute((rx / rz) * y) * sgnRx
            Y = sgnRy * np.sqrt((pow(ry, 2)/4) - pow(y, 2) * ((pow(rx, 2) + pow(rz, 2))/pow(rz, 2)))
            Z = np.absolute(y) * sgnRz 
            self.ax.plot(X, Y, Z, color = "blue", label = 'β')
            self.ax.text(X[500], Y[500], Z[500], 'β', style='italic', fontweight='bold', color = "black", fontsize=12)

            # ->    Curva con respecto al eje z (angulo ɣ)
            # generacion de todos los valores de z 
            z = np.linspace(0, (0.5 * rx * rz)/np.sqrt(pow(rx, 2) + pow(ry, 2) + pow(rz, 2)), 1000) 

            # formulas
            X = np.absolute(z) * sgnRx
            Y = np.absolute((ry / rx) * z) * sgnRy
            Z = sgnRz * np.sqrt((pow(rz, 2)/4) - pow(z, 2) * ((pow(rx, 2) + pow(ry, 2))/pow(rx, 2)))
            self.ax.plot(X, Y, Z, color = "green", label = 'ɣ')
            self.ax.text(X[500], Y[500], Z[500], 'ɣ', style='italic', fontweight='bold', color = "black", fontsize=12)

            plt.legend(ncol = 4, loc = 8, draggable = True)
    
        plt.tight_layout()

    #------------ Función para borrar la gráfica -----------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        plt.clf()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------
    def cerrarGraf(self):
	    plt.close(self.fig)
