# Archivo con el proceso de graficación y animaciones. Practica 05

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
from mpl_toolkits import mplot3d

#------------ Clase para el Canvas ----------------------------------------------------------------------------------#
class ley_Inercia(FigureCanvas):
    #------------------ Función Inicial------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de 1ra ley (muestra) -------------------------------------
    def graficar1raLey_muestra(self):    # Se piden las variables de otra clase para poder trabajarlos.
        V0x = 10
        V0y = 10
        V0z = 10
        tiempo = 5

        posX = []
        posY = []
        posZ = []

        for i in range (0, tiempo*10 + 1, 1):
            posX.append(V0x*float(i/10))
            posY.append(V0y*float(i/10))
            posZ.append(V0z*float(i/10))

        velX = V0x
        velY = V0y
        velZ = V0z

        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("1ra Ley de Newton: Ley de Inercia")  
        self.ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("PosiciónZ [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})

        if(max(posX) > 0):
            self.ax.plot((max(posX), 0), (0, 0), (0, 0), color = "orange", label='X(+)')
            self.ax.plot((0, -max(posX)), (0, 0), (0, 0), color = "red", label='X(-)')
        else:
            self.ax.plot((-min(posX), 0), (0, 0), (0, 0), color = "orange", label='X(+)')
            self.ax.plot((0, min(posX)), (0, 0), (0, 0), color = "red", label='X(-)')
        if(max(posY) > 0): 
            self.ax.plot((0, 0), (max(posY), 0), (0, 0), color = "green", label='Y(+)')
            self.ax.plot((0, 0), (0, -max(posY)), (0, 0), color = "blue", label='Y(-)')
        else:
            self.ax.plot((0, 0), (-min(posY), 0), (0, 0), color = "green", label='Y(+)')
            self.ax.plot((0, 0), (0, min(posY)), (0, 0), color = "blue", label='Y(-)')
        if(max(posZ) > 0):
            self.ax.plot((0, 0), (0, 0), (max(posZ), 0), color = "yellow", label='Z(+)')
            self.ax.plot((0, 0), (0, 0), (0, -max(posZ)), color = "brown", label='Z(-)')
        else:
            self.ax.plot((0, 0), (0, 0), (-min(posZ), 0), color = "yellow", label='Z(+)')
            self.ax.plot((0, 0), (0, 0), (0, min(posZ)), color = "brown", label='Z(-)')

        line, = self.ax.plot(0, 0, 0, color="crimson", linestyle="--", marker="o", label="Ley Inercia") 
        
        for i in range(0, int(len(posX) - 1), 10):
            Q = self.ax.quiver(posX[i], posY[i], posZ[i], velX, velY, velZ, color="darkgoldenrod")   # Vector de velocidad

        Q.set_label("Vector Velocidad")
        plt.legend()    # Muestra las etiquetas

        def animation(i):     # Función para realizar los frames de la animación

            line.set_data(posX[:i], posY[:i])
            line.set_3d_properties(posZ[:i])

            return line,

        global anim
        anim = FuncAnimation(self.fig, func = animation, interval=100, frames=len(posX), repeat=True, blit=True)
        # self.anim = FuncAnimation(self.fig, func = animation, interval=100, frames=len(posX), repeat=True, blit=True)
        self.fig.canvas.draw()        
        self.fig.canvas.flush_events()
        #self.anim.save('Practica05_graf\Ley_Inercia(Prueba).gif')
    #------------ Grafica de 1ra ley (muestra) (FIN) -------------------------------

    #------------ Grafica de 1ra ley --------------------------------------------
    def graficar1raLey(self, posX, posY, posZ, velX, velY, velZ):    # Se piden las variables de otra clase para poder trabajarlos.

        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("1ra Ley de Newton: Ley de Inercia")  
        self.ax.set_xlabel("PosiciónX [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("PosiciónY [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("PosiciónZ [m]", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})

        if(max(posX) > 0):
            self.ax.plot((max(posX), 0), (0, 0), (0, 0), color = "orange", label='X(+)')
            self.ax.plot((0, -max(posX)), (0, 0), (0, 0), color = "red", label='X(-)')
        else:
            self.ax.plot((-min(posX), 0), (0, 0), (0, 0), color = "orange", label='X(+)')
            self.ax.plot((0, min(posX)), (0, 0), (0, 0), color = "red", label='X(-)')
        if(max(posY) > 0): 
            self.ax.plot((0, 0), (max(posY), 0), (0, 0), color = "green", label='Y(+)')
            self.ax.plot((0, 0), (0, -max(posY)), (0, 0), color = "blue", label='Y(-)')
        else:
            self.ax.plot((0, 0), (-min(posY), 0), (0, 0), color = "green", label='Y(+)')
            self.ax.plot((0, 0), (0, min(posY)), (0, 0), color = "blue", label='Y(-)')
        if(max(posZ) > 0):
            self.ax.plot((0, 0), (0, 0), (max(posZ), 0), color = "yellow", label='Z(+)')
            self.ax.plot((0, 0), (0, 0), (0, -max(posZ)), color = "brown", label='Z(-)')
        else:
            self.ax.plot((0, 0), (0, 0), (-min(posZ), 0), color = "yellow", label='Z(+)')
            self.ax.plot((0, 0), (0, 0), (0, min(posZ)), color = "brown", label='Z(-)')

        line, = self.ax.plot(0, 0, 0, color="crimson", linestyle="--", marker="o", label="Ley Inercia") 
        
        for i in range(0, int(len(posX) - 1), 10):
            Q = self.ax.quiver(posX[i], posY[i], posZ[i], velX, velY, velZ, color="darkgoldenrod")   # Vector de velocidad

        Q.set_label("Vector Velocidad")
        plt.legend()    # Muestra las etiquetas

        def animation(i):     # Función para realizar los frames de la animación

            line.set_data(posX[:i], posY[:i])
            line.set_3d_properties(posZ[:i])

            return line,

        global anim
        anim = FuncAnimation(self.fig, func = animation, interval=100, frames=len(posX), repeat=True, blit=True)
        # self.anim = FuncAnimation(self.fig, func = animation, interval=100, frames=len(posX), repeat=True, blit=True)
        self.fig.canvas.draw()        
        self.fig.canvas.flush_events()
        #self.anim.save('Practica05_graf\Ley_Inercia(Prueba).gif')
    #------------ Grafica 1ra Ley (FIN) -----------------------------------------

    #------------ Guardar la gráfica -------------------------------------------------------------
    def guardar_graf(self, direccion):
        anim.save(direccion + "/1raLey.gif")

    #------------ Borrar la gráfica --------------------------------------------------------------

    #------------ Función para borrar la gráfica ---------------------------------
    def vaciar_grafica(self):
        anim.event_source.stop()   # Se agrega para evitar errores al borrar la gráfica
        # self.anim.event_source.stop() 
        self.ax.cla()
        plt.clf()

    #------------ Función para borrar la gráfica (FIN) ---------------------------