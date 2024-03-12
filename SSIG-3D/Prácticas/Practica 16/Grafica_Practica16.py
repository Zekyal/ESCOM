# Archivo con el proceso de graficación y animaciones. Practica 16

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
import numpy as np

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class Tiro_Parabolico(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica (muestra) -------------------------------------
    def graficar_muestra(self):    

        #self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Tiro Parabólico")  
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        # Definimos los parámetros del tiro parabólico
        m = 1  # masa
        g = 9.81  # aceleración debido a la gravedad
        #Dame la velocidad_inicial_X
        vox = 10
        #Dame_la_veloidad_incial_Y
        voy = 10  
        #Dame_la velocidad_inicial_Z
        voz = 50.0 
        tmax = (2*voz)/g
        # (Salida)La distancia final de impacto es: 
        dmax = np.sqrt(pow(vox*tmax,2) + pow(voy*tmax,2) + pow(-g*tmax*tmax/2.0 + voz*tmax,2))
        #Elige una valor de la distancia final, <= que la distancia final de impacto, pord = es el porcentaje de la distancia de impacto pord = (0,1]
        pord = 0.4

        dist = pord *dmax  #distancia del origen a un punto en el plano XY
        ao = np.sqrt(pow(vox,2) + pow(voy,2))  
        tfi = dist/ao  # tiempo final para recorrer la distancia d =  dist
        #print('tmax, tfi =', tmax, tfi)
        #exit(0)
        # No se le pide posición inicial, por  default se tiene:
        Xo = 0
        Yo = 0
        Zo = 0

        # Definimos las ecuaciones de movimiento
        def r_vec(t):
            x = vox * t + Xo
            y = voy * t + Yo
            z = -0.5 * g * t**2 + voz * t + Zo
            return np.array([x, y, z])

        def v_vec(t):
            vx = vox
            vy = voy
            vz = -g * t + voz
            return np.array([vx, vy, vz])

        # Definimos los límites del gráfico
        max_range = 300
        self.ax.set_xlim([0, max_range])
        self.ax.set_ylim([0, max_range])
        self.ax.set_zlim([0, 2*max_range])

        #tmax = (2 * voz) / g  # Calcula el tiempo máximo
        num_frames = 300  # Número de frames para la animación
        time_interval = tfi / num_frames  # Calcula el intervalo de tiempo entre cada frame

        def update(frame):
            # Borramos los datos anteriores
            self.ax.clear()
            
            # Añadimos el plano XY en color 10
            X, Y = np.meshgrid(np.linspace(0, max_range, 2), np.linspace(0, max_range, 2))
            Z = np.zeros_like(X)
            self.ax.plot_surface(X, Y, Z, color='C1', alpha=0.3)
            
            # Añadimos la trayectoria hasta el tiempo actual
            current_time = frame * time_interval
            t = np.linspace(0, current_time, 100)
            r = np.array([r_vec(ti) for ti in t])
            self.ax.plot(r[:,0], r[:,1], r[:,2], 'b')
            
        # Calcular las posiciones finales xf y yf
            xf = vox * tfi
            yf = voy * tfi
            zf =  -0.5 * g * tfi**2 + voz * tfi

        # Añadimos el punto más alto en color rojo
            t_max_altura = voz / g
            X_max = vox * t_max_altura
            Y_max = voy * t_max_altura
            Z_max = -0.5 * g * t_max_altura**2 + voz * t_max_altura
            self.ax.scatter(X_max, Y_max, Z_max, color='r', marker='o')
            self.ax.text(X_max, Y_max, Z_max, f'altura_max = ({X_max:.2f}, {Y_max:.2f}, {Z_max:.2f})', color = 'blue')
            self.ax.scatter(xf, yf, zf, color='g', marker='o')
            self.ax.text(xf, yf, zf, f'posición_final = ({xf:.2f}, {yf:.2f}, {zf:.2f})', color = 'blue')


            # Dibujar la línea roja en el plano XY
            self.ax.plot([Xo, xf], [Yo, yf], [0, 0], color='red')

            # Añadir etiqueta con la distancia de impacto
            d_final = np.sqrt(pow(xf,2) + pow(yf,2) + pow(zf,2))

            self.ax.text(xf / 4, yf / 4, 0, f'd_final = {d_final:.2f}', color='red')


            # Añadimos una etiqueta con el tiempo actual
            self.ax.text2D(0.05, 0.95, f'Tiempo: {current_time:.2f} s', transform=self.ax.transAxes)

            return self.ax

        self.ani = FuncAnimation(self.fig, update, frames=num_frames, interval=time_interval*1000, blit=False, repeat=False)
        plt.tight_layout()

    #------------ Grafica (muestra) (FIN) -------------------------------

    #------------ Grafica Tiro Parabólico --------------------------------
    def graficarTiroPar(self, vox, voy, voz, pord):    # Se piden las variables de otra clase para poder trabajarlos.

        plt.suptitle("Tiro Parabólico")  
        self.ax.set_xlabel("Posición_X [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z [m]", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        # Definimos los parámetros del tiro parabólico
        m = 1  # masa
        g = 9.81  # aceleración debido a la gravedad
        tmax = (2*voz)/g
        # (Salida)La distancia final de impacto es: 
        dmax = np.sqrt(pow(vox*tmax,2) + pow(voy*tmax,2) + pow(-g*tmax*tmax/2.0 + voz*tmax,2))

        dist = pord *dmax  #distancia del origen a un punto en el plano XY
        ao = np.sqrt(pow(vox,2) + pow(voy,2))  
        tfi = dist/ao  # tiempo final para recorrer la distancia d =  dist
        #print('tmax, tfi =', tmax, tfi)
        #exit(0)
        # No se le pide posición inicial, por  default se tiene:
        Xo = 0
        Yo = 0
        Zo = 0

        # Definimos las ecuaciones de movimiento
        def r_vec(t):
            x = vox * t + Xo
            y = voy * t + Yo
            z = -0.5 * g * t**2 + voz * t + Zo
            return np.array([x, y, z])

        def v_vec(t):
            vx = vox
            vy = voy
            vz = -g * t + voz
            return np.array([vx, vy, vz])
        
        #Calcular las posiciones finales xf y yf
        xf1 = vox * tfi
        yf1 = voy * tfi
        zf1 =  -0.5 * g * tfi**2 + voz * tfi


        # Definimos los límites del gráfico
        max_range = np.sqrt(xf1*xf1 + yf1*yf1 + zf1+zf1)
        self.ax.set_xlim([0, max_range])
        self.ax.set_ylim([0, max_range])
        self.ax.set_zlim([0, 2*max_range])

        #tmax = (2 * voz) / g  # Calcula el tiempo máximo
        num_frames = 300  # Número de frames para la animación
        time_interval = tfi / num_frames  # Calcula el intervalo de tiempo entre cada frame

        def update(frame):
            # Borramos los datos anteriores
            self.ax.clear()
            
            # Añadimos el plano XY en color 10
            X, Y = np.meshgrid(np.linspace(0, max_range, 2), np.linspace(0, max_range, 2))
            Z = np.zeros_like(X)
            self.ax.plot_surface(X, Y, Z, color='C1', alpha=0.3)
            
            # Añadimos la trayectoria hasta el tiempo actual
            current_time = frame * time_interval
            t = np.linspace(0, current_time, 100)
            r = np.array([r_vec(ti) for ti in t])
            self.ax.plot(r[:,0], r[:,1], r[:,2], 'b')
            
        # Calcular las posiciones finales xf y yf
            xf = vox * tfi
            yf = voy * tfi
            zf =  -0.5 * g * tfi**2 + voz * tfi

        # Añadimos el punto más alto en color rojo
            t_max_altura = voz / g
            X_max = vox * t_max_altura
            Y_max = voy * t_max_altura
            Z_max = -0.5 * g * t_max_altura**2 + voz * t_max_altura
            self.ax.scatter(X_max, Y_max, Z_max, color='r', marker='o')
            self.ax.text(X_max, Y_max, Z_max, f'altura_max = ({X_max:.2f}, {Y_max:.2f}, {Z_max:.2f})', color = 'blue')
            self.ax.scatter(xf, yf, zf, color='g', marker='o')
            self.ax.text(xf, yf, zf, f'posición_final = ({xf:.2f}, {yf:.2f}, {zf:.2f})', color = 'blue')


            # Dibujar la línea roja en el plano XY
            self.ax.plot([Xo, xf], [Yo, yf], [0, 0], color='red')

            # Añadir etiqueta con la distancia de impacto
            d_final = np.sqrt(pow(xf,2) + pow(yf,2) + pow(zf,2))

            self.ax.text(xf / 4, yf / 4, 0, f'd_final = {d_final:.2f}', color='red')


            # Añadimos una etiqueta con el tiempo actual
            self.ax.text2D(0.05, 0.95, f'Tiempo: {current_time:.2f} s', transform=self.ax.transAxes)

            return self.ax

        self.ani = FuncAnimation(self.fig, update, frames=num_frames, interval=time_interval*1000, blit=False, repeat=False)
        plt.tight_layout()

    #------------ Grafica Ángulo Sólido (FIN) -----------------------------------------

    #------------ Función para borrar la gráfica ---------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        plt.clf()

    #------------ Función para borrar la gráfica (FIN) ---------------------------