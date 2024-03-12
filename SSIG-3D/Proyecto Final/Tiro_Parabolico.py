## Archivo para el módulo de "Tiro Parabólico"
from PyQt5 import QtWidgets

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
from mpl_toolkits import mplot3d
import numpy as np

#*************************** Clase de Tiro Parabólico ******************************************************************************************************************
class Tiro_Parabolico(FigureCanvas):
    #------------------ Función Inicial---------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Tiro parabólico ---------------------------------------------------------------------------------------------------------------------------
    def graficar_tiro_parabolico(self, x0, y0, z0, V0x, V0y, V0z, tiempo, usuario, tabla):    
        self.ax.set_title("Hecho por: " + usuario, loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Ejemplo de tiro parabólico")  
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        posX = []   # Lista para guardar los valores de las posiciones de X
        posY = []   # Lista para guardar los valores de las posiciones de Y
        posZ = []   # Lista para guardar los valores de las posiciones de Z

        velX = []   # Lista para guardar los valores de las velocidades de X
        velY = []   # Lista para guardar los valores de las velocidades de Y
        velZ = []   # Lista para guardar los valores de las velocidades de Z

        gravedad = 9.81     # Valor de la gravedad.
        calculando = str(tiempo)
        decimales = calculando.split(".")

        entero = decimales[0][0]
        primerDec = decimales[1][0]

        # Se hace la comprobación dado que no considera en los casos de tener "0" en el segundo decimal        
        if (len(decimales[1]) == 1):    
            segDec = 0
        else:
            segDec = decimales[1][1:]

        numero_filas = int(entero)*100 + int(primerDec)*10 + int(segDec) + 1 # checar

        for t in range(0, numero_filas, 1):
            tabla.setRowCount(t+1)
            tabla.setItem(t, 0, QtWidgets.QTableWidgetItem(str(t/100)))    # Mete los valores a la tabla llamada "tabla_tiro_par" en la columna Tiempo
            posX.append(V0x*float(t/100) + x0)
            tabla.setItem(t, 1, QtWidgets.QTableWidgetItem(str(posX[t])))    # Mete los valores a la tabla llamada "tabla_tiro_par" en la columna Posición X
            posY.append(V0y*float(t/100) + y0)
            tabla.setItem(t, 2, QtWidgets.QTableWidgetItem(str(posY[t])))    # Mete los valores a la tabla llamada "tabla_tiro_par" en la columna Posición Y
            posZ.append(-1/2*gravedad*float(pow(t/100, 2)) + V0z*float(t/100) + z0)
            tabla.setItem(t, 3, QtWidgets.QTableWidgetItem(str(posZ[t])))    # Mete los valores a la tabla llamada "tabla_tiro_par" en la columna Posición Z
            velX.append(V0x)
            tabla.setItem(t, 4, QtWidgets.QTableWidgetItem(str(velX[t])))    # Mete los valores a la tabla llamada "tabla_tiro_par" en la columna Velocidad X
            velY.append(V0y)
            tabla.setItem(t, 5, QtWidgets.QTableWidgetItem(str(velY[t])))    # Mete los valores a la tabla llamada "tabla_tiro_par" en la columna Velocidad Y
            velZ.append(-gravedad*(t/100) + V0z)
            tabla.setItem(t, 6, QtWidgets.QTableWidgetItem(str(velZ[t])))    # Mete los valores a la tabla llamada "tabla_tiro_par" en la columna Velocidad Z
            if ((t > 0) and (posZ[t] <= 0)):
                numero_filas = tabla.rowCount()
                break

        tiempo = round(tiempo)

        max_axis_x = max(posX)
        min_axis_x = min(posX)
        max_axis_y = max(posY)
        min_axis_y = min(posY)
        max_axis_z = max(posZ)

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

        self.ax.plot((0, 0), (0, 0), (0, 1.25*max_axis_z), color = "slateblue", label='Z')
        self.ax.text(0, 0, 1.25*max_axis_z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)

        # Dibujando la superficie
        # Crear el arreglo de ceros de dimensión (n, m)
        n = round(1.25*max_axis_x)
        m = round(1.25*max_axis_x)
        arr = np.zeros((n, m))

        # Crear las coordenadas x, y
        x = np.linspace(1.25*min_axis_x, 1.25*max_axis_x, n)
        y = np.linspace(1.25*min_axis_y, 1.25*max_axis_y, m)

        # Crear la malla de coordenadas
        X, Y = np.meshgrid(x, y)

        self.ax.plot_surface(X, Y, arr, color = 'peru', alpha = 0.4)

        line, = self.ax.plot(0, 0, 0, marker='o', label='Tiro Parabólico', color='black') 

        for i in range(0, int(len(posX) - 1), 100):
            Q = self.ax.quiver(posX[i], posY[i], posZ[i], velX[i], velY[i], velZ[i], color='coral') # Graficamos los vectores de velocidad

        Q.set_label("-> Vector Velocidad")
        plt.tight_layout()
        plt.legend(ncol = 3, loc = 8, draggable = True) # Muestra las etiquetas

        def animation(i):     # Función para realizar los frames de la animación

            line.set_data(posX[:i], posY[:i])
            line.set_3d_properties(posZ[:i])

            return line,

        global anim
        anim = FuncAnimation(self.fig, func = animation, interval=10, frames=numero_filas, repeat=False, blit=True)
        self.fig.canvas.draw()        
        self.fig.canvas.flush_events()

    #------------ Función para guardar la gráfica ----------------------------------------------------------------------------------------------------------------------
    def guardar_graf(self, direccion):
        anim.save(direccion + '/TiroParabolico.gif')
        plt.savefig(direccion + "/TiroParabolico.jpg")
    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
