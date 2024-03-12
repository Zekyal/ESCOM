# Archivo con el proceso de graficación y animaciones. Practica 05

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
from mpl_toolkits import mplot3d
import numpy as np

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Polea(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica (muestra) -------------------------------------
    def graficar_muestra(self, ace):    
        #Dame la longitud del plano inclinado que desas trabajar:
        l = 500
        #Dame el valor de la masa m1 (masa sobre la pendiente)
        m1 = 5
        m2 =  10
        #gravedad
        g = 9.81
        #muk =  Dame el coeficiente de fricción cinética
        muk= 0.57
        #mus = Dame el coeficiente de fricción estática
        mus = 1.43*muk
        #Dame el ángulo de la pendiente
        theta =  50
        theta_0 = np.arctan(mus)
        theta_0 = np.degrees(theta_0)

        theta_r = np.radians(theta)

        theta = theta_r
        N = m1*g*np.cos(theta)
        Fxs = mus*N # Fuerza de fricción estática en X
        Fxk = muk*N # Fuerza de fricción cinética en X
        wx = m1*g*np.sin(theta)

        #fuerza minima necesaria para estar en movimiento ascendente
        feqxk =  Fxk + wx

        w2 = m2*g
        #Calculamos la aceleración en X
        acx = (1.0/(m1+m2))*(w2 - feqxk)
        if acx<= 0:
            if wx <= (w2 + Fxs) and acx <=0:
                acx = 0.0
            else:
                acx =  ((Fxk + w2)-wx)*(1.0/(m1+m2))
        else:
            acx = acx
            ace.setText("Aceleración Final = " + str(acx))

        # Definimos las ecuaciones de movimiento del primer punto en 3D
        def movimiento1(t):
            x1 = 0
            y1 = 0.5*acx*t*t*(np.cos(theta))
            z1 = 0.5*acx*pow(t,2)*(np.sin(theta))

            return x1, y1, z1

        # sea l la longitud del recorrido del cuerpo desplazado sobre el plano

        yf = l*np.cos(theta)
        zf = l*np.sin(theta)
        # Definimos las ecuaciones de movimiento del segundo punto en 3D
        def movimiento2(t):
            x2 = 0.0
            y2 = yf
            z2 = 0.5*zf - acx*0.5*pow(t,2)

            return x2, y2, z2

        # Creamos la figura y el objeto para la animación
        punto1, = self.ax.plot([], [], [], 'rs', markersize=10, label ="m1")
        punto2, = self.ax.plot([], [], [], 'gs', markersize=10, label ="m2")
        trayectoria1, = self.ax.plot([], [], [], 'r--')
        trayectoria2, = self.ax.plot([], [], [], 'b--')

        ##############################################################

        # Agregar etiquetas a los ejes
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")
        self.ax.grid(False)

        self.ax.set_xlim(-0.1*l, 0.1*l)
        self.ax.set_ylim(-0.1*l, l)
        self.ax.set_zlim(0, l)

        plt.legend()
        plt.tight_layout()

        #===================================================
        #Genera el triángulo

        x3 = [0,0,0,0,]
        y3 = [0, l*np.cos(theta), l*np.cos(theta),0]
        z3 = [0, l*np.sin(theta), 0,0]

        self.ax.scatter(x3, y3, z3, c='r', marker='o')

        plt.plot(x3,y3,z3, color='blue')

        # Inicializamos las listas para almacenar las coordenadas de los puntos y las trayectorias
        x1_punto1 = []
        y1_punto1 = []
        z1_punto1 = []
        x1_trayectoria1 = []
        y1_trayectoria1 = []
        z1_trayectoria1 = []

        x2_punto2 = []
        y2_punto2 = []
        z2_punto2 = []
        x2_trayectoria2 = []
        y2_trayectoria2 = []
        z2_trayectoria2 = []

        # Definimos la función que actualizará la posición de los puntos en cada fotograma
        def actualizar(i):
            x1, y1, z1 = movimiento1(i)
            x2, y2, z2 = movimiento2(i)
            
            # Actualizamos las coordenadas y las trayectorias del primer punto
            x1_punto1.append(x1)
            y1_punto1.append(y1)
            z1_punto1.append(z1)
            punto1.set_data(x1, y1)
            punto1.set_3d_properties(z1)
            x1_trayectoria1.append(x1)
            y1_trayectoria1.append(y1)
            z1_trayectoria1.append(z1)
            trayectoria1.set_data(x1_trayectoria1, y1_trayectoria1)
            trayectoria1.set_3d_properties(z1_trayectoria1)

            # Actualizamos las coordenadas y las trayectorias del segundo punto
            x2_punto2.append(x2)
            y2_punto2.append(y2)
            z2_punto2.append(z2)
            punto2.set_data(x2, y2)
            punto2.set_3d_properties(z2)
            x2_trayectoria2.append(x2)
            y2_trayectoria2.append(y2)
            z2_trayectoria2.append(z2)
            trayectoria2.set_data(x2_trayectoria2, y2_trayectoria2)
            trayectoria2.set_3d_properties(z2_trayectoria2)

            if z2 >=l*np.sin(theta) or z2 <=0.0:
                ani.event_source.stop()

            return punto1, punto2, trayectoria1, trayectoria2

        #Crea la animación
        global ani
        ani = FuncAnimation(self.fig, actualizar, frames=np.linspace(0, 300, 3000),
                                    interval=100, blit=True)

    #------------ Grafica (muestra) (FIN) -------------------------------

    #------------ Grafica Polea --------------------------------------------
    def graficarPolea(self, m1, m2, l, muk, theta, ace):    # Se piden las variables de otra clase para poder trabajarlos.

        #self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Polea y Contrapeso")  
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        #gravedad
        g = 9.81
        #mus = Dame el coeficiente de fricción estática
        mus = 1.43*muk
        #Dame el ángulo de la pendiente
        theta_0 = np.arctan(mus)
        theta_0 = np.degrees(theta_0)

        theta_r = np.radians(theta)

        theta = theta_r
        N = m1*g*np.cos(theta)
        Fxs = mus*N # Fuerza de fricción estática en X
        Fxk = muk*N # Fuerza de fricción cinética en X
        wx = m1*g*np.sin(theta)

        #fuerza minima necesaria para estar en movimiento ascendente
        feqxk =  Fxk + wx

        w2 = m2*g
        #Calculamos la aceleración en X
        acx = (1.0/(m1+m2))*(w2 - feqxk)
        if acx<= 0:
            if wx <= (w2 + Fxs) and acx <=0:
                acx = 0.0
                ace.setText("Aceleración Final = " + str(acx))
            else:
                acx =  ((Fxk + w2)-wx)*(1.0/(m1+m2))
                ace.setText("Aceleración Final = " + str(acx))
        else:
            acx = acx
            ace.setText("Aceleración Final = " + str(acx))

        # Definimos las ecuaciones de movimiento del primer punto en 3D
        def movimiento1(t):
            x1 = 0
            y1 = 0.5*acx*t*t*(np.cos(theta))
            z1 = 0.5*acx*pow(t,2)*(np.sin(theta))

            return x1, y1, z1

        # sea l la longitud del recorrido del cuerpo desplazado sobre el plano

        xf = l*np.cos(theta)
        yf = l*np.cos(theta)
        zf = l*np.sin(theta)
        # Definimos las ecuaciones de movimiento del segundo punto en 3D
        def movimiento2(t):
            x2 = 0.0
            y2 = yf
            z2 = 0.5*zf - acx*0.5*pow(t,2)

            return x2, y2, z2

        # Creamos la figura y el objeto para la animación
        punto1, = self.ax.plot([], [], [], 'rs', markersize=10, label = "m1")
        punto2, = self.ax.plot([], [], [], 'gs', markersize=10, label = "m2")
        trayectoria1, = self.ax.plot([], [], [], 'r--')
        trayectoria2, = self.ax.plot([], [], [], 'b--')

        ##############################################################

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")
        self.ax.grid(False)

        self.ax.set_xlim(-0.1*l, 0.1*l)
        self.ax.set_ylim(-0.1*l, l)
        self.ax.set_zlim(0, l)

        #===================================================
        #Genera el triángulo

        x3 = [0,0,0,0,]
        y3 = [0, l*np.cos(theta), l*np.cos(theta),0]
        z3 = [0, l*np.sin(theta), 0,0]

        self.ax.scatter(x3, y3, z3, c='r', marker='o')

        plt.plot(x3,y3,z3, color='blue')
        plt.legend()
        plt.tight_layout()

        # Inicializamos las listas para almacenar las coordenadas de los puntos y las trayectorias
        x1_punto1 = []
        y1_punto1 = []
        z1_punto1 = []
        x1_trayectoria1 = []
        y1_trayectoria1 = []
        z1_trayectoria1 = []

        x2_punto2 = []
        y2_punto2 = []
        z2_punto2 = []
        x2_trayectoria2 = []
        y2_trayectoria2 = []
        z2_trayectoria2 = []



        # Definimos la función que actualizará la posición de los puntos en cada fotograma
        def actualizar(i):
            x1, y1, z1 = movimiento1(i)
            x2, y2, z2 = movimiento2(i)
            
            # Actualizamos las coordenadas y las trayectorias del primer punto
            x1_punto1.append(x1)
            y1_punto1.append(y1)
            z1_punto1.append(z1)
            punto1.set_data(x1, y1)
            punto1.set_3d_properties(z1)
            x1_trayectoria1.append(x1)
            y1_trayectoria1.append(y1)
            z1_trayectoria1.append(z1)
            trayectoria1.set_data(x1_trayectoria1, y1_trayectoria1)
            trayectoria1.set_3d_properties(z1_trayectoria1)

            # Actualizamos las coordenadas y las trayectorias del segundo punto
            x2_punto2.append(x2)
            y2_punto2.append(y2)
            z2_punto2.append(z2)
            punto2.set_data(x2, y2)
            punto2.set_3d_properties(z2)
            x2_trayectoria2.append(x2)
            y2_trayectoria2.append(y2)
            z2_trayectoria2.append(z2)
            trayectoria2.set_data(x2_trayectoria2, y2_trayectoria2)
            trayectoria2.set_3d_properties(z2_trayectoria2)

            if z2 >=l*np.sin(theta) or z2 <=0.0:
                ani.event_source.stop()
            
            return punto1, punto2, trayectoria1, trayectoria2

        #Crea la animación
        global ani
        ani = FuncAnimation(self.fig, actualizar, frames=np.linspace(0, 300, 3000),
                                    interval=100, blit=True)

    #------------ Grafica Polea (FIN) -----------------------------------------

    #------------ Función para borrar la gráfica ---------------------------------
    def vaciar_grafica(self):
        ani.event_source.stop()   # Se agrega para evitar errores al borrar la gráfica
        self.ax.cla()
        plt.clf()

    #------------ Función para borrar la gráfica (FIN) ---------------------------