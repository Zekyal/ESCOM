# Archivo con el proceso de graficación y animaciones. Practica 09

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
import numpy as np

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class ley_dinamica(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    #------------ Grafica Normal  -----------------------------------------------
    def graficaNormal(self, thetha_v, x, y, acx, t):    # Se piden las variables de otra clase para poder trabajarlos.
        posX = []
        posY = []
        self.ax.set_title('¿El objeto se moverá?', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.grid()  # Asigna la cudarícula
        plt.axvline(0, color='black') # Dibuja un eje en y
        plt.axhline(0, color='black') # Dibuja un eje en x
        self.ax.set_xlim(-x-2, x+2)     # Inserta límites al eje X para los valores positivos
        self.ax.set_ylim(-y-2, y+2)     # Inserta límites al eje Y para los valores positivos

        plt.plot([0, x],[0, y], color="green")
        plt.plot([0, -x],[0, -y], color="green")
        plt.plot([x, x],[y, -y], color="green")
        plt.plot([-x, x],[-y, -y], color="green")
        for i in range(0, t, 1):
            posX.append(-(acx*np.cos(thetha_v)*pow(i, 2))/2)
            posY.append(-(acx*np.sin(thetha_v)*pow(i, 2))/2)

        plt.plot(0, 0, marker="o", label='Objeto', color ="indigo")    # objeto en movimiento
        plt.legend() # Muestra las etiquetas

        self.fig.tight_layout()
    #------------ Grafica Normal (FIN) -----------------------------------------

    #------------ Grafica Movimiento  -----------------------------------------------
    def graficaMovimiento(self, thetha, thethaO, thetha_v, x, y, acx, t):    # Se piden las variables de otra clase para poder trabajarlos.
        posX = []
        posY = []
        self.ax.set_title('2da Ley de Newton: Dinámica', loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.grid()  # Asigna la cudarícula
        plt.axvline(0, color='black') # Dibuja un eje en y
        plt.axhline(0, color='black') # Dibuja un eje en x
        self.ax.set_xlim(-x-2, x+2)     # Inserta límites al eje X para los valores positivos
        self.ax.set_ylim(-y-2, y+2)     # Inserta límites al eje Y para los valores positivos

        plt.plot([0, x],[0, y], color="green")
        plt.plot([0, -x],[0, -y], color="green")
        plt.plot([x, x],[y, -y], color="green")
        plt.plot([-x, x],[-y, -y], color="green")
        for i in range(0, t, 1):
            posX.append(-(acx*np.cos(thetha_v)*pow(i, 2))/2)
            posY.append(-(acx*np.sin(thetha_v)*pow(i, 2))/2)

        line, = plt.plot(0, 0, marker="o", label='Objeto', color ="indigo")    # objeto en movimiento
        plt.legend() # Muestra las etiquetas

        def animation(i):     # Función para realizar los frames de la animación
            x_data1 = []
            y_data1 = []
            x_data1.append(posX[i])  # Inserta punto a punto los valores a las listas vacias.
            y_data1.append(posY[i])
            line.set_xdata(x_data1)
            line.set_ydata(y_data1)
            return line,

        if (thetha > np.degrees(thethaO)):
            self.anim = FuncAnimation(self.fig, animation, interval=1000, frames=len(posX), repeat=True)
        self.fig.tight_layout()
        self.fig.canvas.draw()
    #------------ Grafica Movimiento (FIN) -----------------------------------------
    def cerrarGraf(self):
	    plt.close(self.fig)