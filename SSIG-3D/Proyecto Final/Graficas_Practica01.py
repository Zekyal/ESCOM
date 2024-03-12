# Archivo con el proceso de graficación y animaciones. Practica01.

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Canvas_grafica(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    #------------ Grafica de Posición (Puntos) ----------------------------------
    def graficarPosicionNormal(self, pos01, tiem01):    # Se piden las variables de otra clase para poder trabajarlos.
        x_data1 = []    # Se crea un array vacio para insertar los valores de la lista "tiem01" -> "t"
        y_data1 = []    # Se crea un array vacio para insertar los valores de la lista "pos01" -> "pos"
        self.ax.set_title('Gráfica de Posiciones', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.grid()  # Asigna la cudarícula
        plt.axvline(0, color='black') # Dibuja un eje en y
        plt.axhline(0, color='black') # Dibuja un eje en x
        self.ax.set_ylim(-1, 1)     # Inserta límites al eje Y 
        if float(max(pos01)) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_xlim(float(min(pos01)), float(max(pos01)))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_xlim(float(max(pos01)), float(min(pos01))) 

        line, = self.ax.plot(0, 0, marker = 'o', color='red', label='Posición')  # Grafica los puntos con "o" (círculos)
        plt.legend() # Muestra las etiquetas
        self.fig.tight_layout() # Ajusta la gráfica al espacio disponible.

        def animation_frame_Pos01(i):     # Función para realizar los frames de la animación
            x_data1.clear()     # Vacía las listas para solo mostrar un valor
            y_data1.clear()
            x_data1.append(float(pos01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data1.append(float(tiem01[0]))
            if (((pos01[i]) >= 0) and (pos01[i+1] >= pos01[i])): # Cambiamos los símbolos y colores de la gráfica en la subida
                line.set_color('green')
            else:
                line.set_color('red')   # Cambiamos los símbolos y colores de la gráfica al caer
            line.set_xdata(x_data1)
            line.set_ydata(y_data1)

            return line,   

        animationPos = FuncAnimation(self.fig, func=animation_frame_Pos01, frames=99, interval=100, repeat = True) # Función para aplicar la animación
        animationPos.save('Practica01_grafs\Posicion01.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Posición (FIN) -------------------------------------
    def cerrarGraf(self):
        plt.close(self.fig)
    

class Canvas_grafica2(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    #------------ Grafica de Velocidad (Vectores) ------------------------------------
    def graficarVelocidadNormal(self, pos01, vel01, tiem01):
        x_data2 = []    # Se crea un array vacio para insertar los valores de la lista "vel01" -> "vel"
        y_data2 = []    # Se crea un array vacio para insertar los valores de la lista "velY01" -> "velY"
        self.ax.set_title('Gráfica de Posiciones con Vectores de Velocidad', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Título de la Gráfica
        self.ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.grid()  # Asigna la cudarícula
        plt.axvline(0, color='black') # Dibuja un eje en y
        plt.axhline(0, color='black') # Dibuaj un eje en x
        self.ax.set_ylim(-1, 1)     # Inserta límites al eje Y para los valores positivos
        if float(max(pos01)) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_xlim(float(min(pos01)), float(max(pos01)))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_xlim(float(max(pos01)), float(min(pos01))) 

        line, = plt.plot(0, 0, marker = 'o', color='red' ,label='Posición')  # Grafica los puntos con ">" 
        Qr = self.ax.quiver(0, 0, 0, 0, color= 'blue', units='inches', label='Vector Velocidad')   # Para la creación de flechas
        plt.legend()
        self.fig.tight_layout()

        def animation_frame_Vel01(i):     # Función para realizar los frames de la animación
            x_data2.clear()
            y_data2.clear()
            x_data2.append(float(pos01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data2.append(float(tiem01[0]))
            if (((pos01[i]) >= 0) and (pos01[i+1] >= pos01[i])): # Cambiamos los símbolos y colores de la gráfica en la subida
                line.set_color('green')
                Qr.set_color('blue')
            else:
                line.set_color('red')   # Cambiamos los símbolos y colores de la gráfica al caer
                Qr.set_color('purple')

            line.set_xdata(x_data2)
            line.set_ydata(y_data2)

            u = float(vel01[i])
            v = 0
            Qr.set_offsets([[x_data2, y_data2]])    # Actualiza los valores de la posición inicial de la quiver.
            Qr.set_UVC(u, v)        # Actualiza los valores de la posición final de la quiver.

            return line, Qr,

        animationVel01 = FuncAnimation(self.fig, func=animation_frame_Vel01, frames=99, interval=100, repeat = True)    # Función para aplicar la animación
        animationVel01.save('Practica01_grafs\Velocidad01.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Velocidad (FIN) ----------------------------------------
    def cerrarGraf(self):
        plt.close(self.fig)

class Canvas_grafica3(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    #------------ Grafica de Aceleración (Vectores) -----------------------------------
    def graficarAceleracionNormal(self, pos01, ace01, tiem01):
        x_data3 = []    # Se crea un array vacio para insertar los valores de la lista "tiem01" -> "t"
        y_data3 = []    # Se crea un array vacio para insertar los valores de la lista "ace01" -> "ace"
        self.ax.set_title('Gráfica de Posiciones con Vectores de Aceleración', loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'}) # Título de la Gráfica
        self.ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})  # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.grid()  # Asigna la cudarícula
        plt.axvline(0, color='black') # Dibuja un eje en y
        plt.axhline(0, color='black') # Dibuaj un eje en x
        self.ax.set_ylim(-1, 1)     # Inserta límites al eje Y para los valores positivos
        if float(max(pos01)) > 0:        # Ajusta los ejes en caso de tener valores negativos
            self.ax.set_xlim(float(min(pos01)), float(max(pos01)))     # Inserta límites al eje X para los valores positivos
        else:
            self.ax.set_xlim(float(max(pos01)), float(min(pos01))) 

        line, = plt.plot(0, 0, marker = 'o', color='red', label='Posición')  # Grafica los puntos con ">" 
        Qr = self.ax.quiver(0, 0, 0, 0, color= 'blue', units='inches', label='Vector Aceleración')   # Para la creación de flechas
        plt.legend()
        self.fig.tight_layout()

        def animation_frame_Ace01(i):     # Función para realizar los frames de la animación
            x_data3.clear()
            y_data3.clear()
            x_data3.append(float(pos01[i]))  # Inserta punto a punto los valores a las listas vacias.
            y_data3.append(float(tiem01[0]))

            if (((pos01[i]) >= 0) and (pos01[i+1] >= pos01[i])): # Cambiamos los símbolos y colores de la gráfica en la subida
                line.set_color('purple')
                Qr.set_color('pink')
            else:
                line.set_color('brown')   # Cambiamos los símbolos y colores de la gráfica al caer
                Qr.set_color('orange')

            line.set_xdata(x_data3)
            line.set_ydata(y_data3)

            u = float(ace01[i])
            v = 0
            Qr.set_offsets([[x_data3, y_data3]])
            Qr.set_UVC(u, v)

            return line, Qr,

        animationAce01 = FuncAnimation(self.fig, func=animation_frame_Ace01, frames=99, interval=100, repeat = True) # Función para aplicar la animación
        animationAce01.save('Practica01_grafs\Aceleracion01.gif')   # Guarda la animación en un archivo de tipo ".gif"
    #------------ Grafica de Aceleración (FIN) --------------------------------------
    def cerrarGraf(self):
        plt.close(self.fig)
