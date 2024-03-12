# Archivo con el proceso de graficación y animaciones.

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
import numpy as np

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Caida_libre(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    #------------ Grafica de Posición (Puntos) ----------------------------------
    def graficarPosicionY(self, pos, tempo):    # Se piden las variables de otra clase para poder trabajarlos.
        x_data1 = []    # Se crea un array vacio para insertar los valores de la lista "tempo" -> "t"
        y_data1 = []    # Se crea un array vacio para insertar los valores de la lista "pos" -> "pos"
        self.ax.set_title('Gráfica de Caida Libre', loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.grid()  # Asigna la cudarícula
        plt.axvline(0, color='black') # Dibuja un eje en y
        plt.axhline(0, color='black') # Dibuja un eje en x
        self.ax.set_xlim(-1, 1)     # Inserta límites al eje X
        if float(max(pos)) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_ylim(float(min(pos)), float(max(pos)))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_ylim(float(max(pos)), float(min(pos))) 

        line, = self.ax.plot(0, 0, marker = 'o', color='red', label='Posición')  # Grafica los puntos con "o" (círculos)
        plt.legend() # Muestra las etiquetas

        def animation_frame_Pos(i):     # Función para realizar los frames de la animación
            x_data1.clear()     # Vacía las listas para solo mostrar un valor
            y_data1.clear()
            x_data1.append(float(tempo[0]))  # Inserta punto a punto los valores a las listas vacias.
            y_data1.append(float(pos[i]))
            if (((pos[i]) >= 0) and (pos[i+1] >= pos[i])): # Cambiamos los símbolos y colores de la gráfica en la subida
                line.set_color('green')
            else:
                line.set_color('red')   # Cambiamos los símbolos y colores de la gráfica al caer
            line.set_xdata(x_data1)
            line.set_ydata(y_data1)
            return line,   

        self.animationPos = FuncAnimation(self.fig, func=animation_frame_Pos, frames=len(tempo)-1, interval=100, repeat = True) # Función para aplicar la animación
        #animationPos.save('Practica01_grafs\Posicion01.gif')   # Guarda la animación en un archivo de tipo ".gif"
        self.fig.tight_layout()
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
    #------------ Grafica de Posición (FIN) -------------------------------------


class Caida_libre2(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    #------------ Grafica de Velocidad (Vectores) ------------------------------------
    def graficarVelocidadY(self, pos, vel, tempo):
        x_data1 = []    # Se crea un array vacio para insertar los valores de la lista "tempo" -> "t"
        y_data1 = []    # Se crea un array vacio para insertar los valores de la lista "pos" -> "pos"
        self.ax.set_title('Gráfica de Caida Libre con Vector de Velocidad', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.grid()  # Asigna la cudarícula
        plt.axvline(0, color='black') # Dibuja un eje en y
        plt.axhline(0, color='black') # Dibuja un eje en x
        self.ax.set_xlim(-1, 1)     # Inserta límites al eje X
        if float(max(pos)) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_ylim(float(min(pos)), float(max(pos)))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_ylim(float(max(pos)), float(min(pos))) 

        line, = self.ax.plot(0, 0, marker = 'o', color='red', label='Posición')  # Grafica los puntos con "o" (círculos)
        Qr = self.ax.quiver([0, 0], [0, 0], 0, 10, color= 'blue', units='inches', label='Vector Velocidad')   # Para la creación de flechas
        plt.legend() # Muestra las etiquetas

        def animation_frame_Vel(i):     # Función para realizar los frames de la animación
            x_data1.clear()
            y_data1.clear()
            x_data1.append(float(tempo[0]))  # Inserta punto a punto los valores a las listas vacias.
            y_data1.append(float(pos[i]))
            if (((pos[i]) >= 0) and (pos[i+1] >= pos[i])): # Cambiamos los símbolos y colores de la gráfica en la subida
                line.set_color('green')
            else:
                line.set_color('red')   # Cambiamos los símbolos y colores de la gráfica al caer

            if (((vel[i]) >= 0) and (vel[i+1] >= vel[i])): # Cambiamos los símbolos y colores de la gráfica en la subida
                Qr.set_color('blue')
            else:
                Qr.set_color('purple')

            line.set_xdata(x_data1)
            line.set_ydata(y_data1)

            u = 0
            v = vel[i]
            y = 1
            Qr.set_offsets([[x_data1, y_data1]])    # Actualiza los valores de la posición inicial de la quiver.
            Qr.set_UVC(u, v, y)        # Actualiza los valores de la posición final de la quiver.

            return line, Qr,

        self.animationVel = FuncAnimation(self.fig, func=animation_frame_Vel, frames=len(tempo)-1, interval=100, repeat = True)    # Función para aplicar la animación
        self.fig.tight_layout()
        self.fig.canvas.draw()
    #------------ Grafica de Velocidad (FIN) ----------------------------------------