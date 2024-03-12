## Archivo para el módulo de "Leyes de Newton"

from PyQt5 import QtWidgets
import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
from mpl_toolkits import mplot3d
from matplotlib.patches import Rectangle
import numpy as np

#*************************** Clase de Primera Ley *********************************************************************************************************************#
class Primera_Ley(FigureCanvas):
    #------------------ Función Inicial---------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Primera Ley -------------------------------------------------------------------------------------------------------------------------------
    def graficar_primera_ley(self, V0x, V0y, V0z, tiempo, usuario, tabla):    
        self.ax.set_title("Hecho por: " + usuario, loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Ejemplo de la 1ra ley de Newton: Inercia") 
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        velX = V0x
        velY = V0y
        velZ = V0z

        posX = []
        posY = []
        posZ = []

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

        tabla.setRowCount(numero_filas)   

        for t in range(0, numero_filas, 1):
            tabla.setItem(t, 0, QtWidgets.QTableWidgetItem(str(t/100)))    # Mete los valores a la tabla llamada "tabla_valores" en la columna Tiempo
            posX.append(V0x*float(t/100))
            tabla.setItem(t, 1, QtWidgets.QTableWidgetItem(str(posX[t])))    # Mete los valores a la tabla llamada "tabla_valores" en la columna Posición X
            posY.append(V0y*float(t/100))
            tabla.setItem(t, 2, QtWidgets.QTableWidgetItem(str(posY[t])))    # Mete los valores a la tabla llamada "tabla_valores" en la columna Posición Y
            posZ.append(V0z*float(t/100))
            tabla.setItem(t, 3, QtWidgets.QTableWidgetItem(str(posZ[t])))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Posición Z
            tabla.setItem(t, 4, QtWidgets.QTableWidgetItem(str(velX)))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Velocidad X
            tabla.setItem(t, 5, QtWidgets.QTableWidgetItem(str(velY)))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Velocidad Y
            tabla.setItem(t, 6, QtWidgets.QTableWidgetItem(str(velZ)))    # Mete los valores a la tabla llamada "tabla_pos" en la columna Velocidad Z

        tiempo = round(tiempo)

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        max_axis_x = max(posX)
        min_axis_x = min(posX)
        max_axis_y = max(posY)
        min_axis_y = min(posY)
        max_axis_z = max(posZ)
        min_axis_z = min(posZ)

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

        if ((max_axis_z >= 0 ) and (min_axis_z >= 0)):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*max_axis_z), color = "slateblue", label='Z')
            self.ax.text(0, 0, 1.25*max_axis_z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        elif ((max_axis_z >= 0 ) and (min_axis_z < 0)):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*max_axis_z), color = "slateblue", label='Z')
            self.ax.plot((0, 0), (0, 0), (1.25*min_axis_z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*max_axis_z, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
            self.ax.text(0, 0, 1.25*min_axis_z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (0, 0), (1.25*min_axis_z, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*min_axis_z, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)

        line, = self.ax.plot(0, 0, 0, color="crimson", linestyle="--", marker="o", label="Ley Inercia") 
        
        for i in range(0, int(len(posX) - 1), 100):
            Q = self.ax.quiver(posX[i], posY[i], posZ[i], velX, velY, velZ, color="darkgoldenrod")   # Vector de velocidad

        Q.set_label("-> Vector Velocidad")
        plt.legend(ncol = 3, loc = 8, draggable = True) # Muestra las etiquetas
        plt.tight_layout()

        def animation(i):     # Función para realizar los frames de la animación

            line.set_data(posX[:i], posY[:i])
            line.set_3d_properties(posZ[:i])

            return line,

        global anim
        anim = FuncAnimation(self.fig, func = animation, interval=100, frames=len(posX), repeat=False, blit=True)
        self.fig.canvas.draw()        
        self.fig.canvas.flush_events()

    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def guardar_graf(self, direccion):
        anim.save(direccion + '/1raLeyInercia.gif')
        plt.savefig(direccion + "/1raLeyInercia.jpg")
    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

#*************************** Clase de Primera Ley (FIN) ***************************************************************************************************************#

#*************************** Clase de Segunda Ley *********************************************************************************************************************#
class Segunda_Ley(FigureCanvas):
    #------------------ Función Inicial---------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Segunda Ley ------------------------------------------------------------------------------------------------------------------------------
    def graficar_seg_ley_muestra(self):    
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Ejemplo de la 2da ley de Newton: Dinámica")  
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

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
            subt1 = r'Aceleración Final = {:.3f}'.format(acx)
            self.ax.text2D(0.05, 0.92, subt1, transform=self.ax.transAxes)


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
        trayectoria2, = self.ax.plot([], [], [], 'y--')

        ##############################################################

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
                x1_punto1.clear()
                y1_punto1.clear()
                z1_punto1.clear()
                x2_punto2.clear()
                y2_punto2.clear()
                z2_punto2.clear()
                x1_trayectoria1.clear()
                y1_trayectoria1.clear()
                z1_trayectoria1.clear()
                x2_trayectoria2.clear()
                y2_trayectoria2.clear()
                z2_trayectoria2.clear()
                self.anim.event_source.stop()
                self.anim = FuncAnimation(self.fig, actualizar, frames=np.linspace(0, 300, 3000),
                                                    interval=100, blit=True)

            return punto1, punto2, trayectoria1, trayectoria2

        #Crea la animación
        self.anim = FuncAnimation(self.fig, actualizar, frames=np.linspace(0, 300, 3000),
                                    interval=100, blit=True)
        
#*************************** Clase de Segunda Ley (FIN) ***************************************************************************************************************#

#*************************** Clase de Tercera Ley *********************************************************************************************************************#
class Tercera_Ley(FigureCanvas):
    #------------------ Función Inicial---------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig, self.ax = plt.subplots()  # Se crea la tabla
        super().__init__(self.fig)

    #------------ Grafica de Tercera Ley -------------------------------------------------------------------------------------------------------------------------------
    def graficar_tercera_ley(self):    
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Ejemplo de la 3ra ley de Newton: Acción y reacción") 

        # Solicitar al usuario los valores de las masas y la aceleración
        m1 = 10
        m2 = 5
        m3 = 14
        a = 5

        # Calcular las fuerzas de acción y reacción
        F12 = (m2 + m3) * a
        F21 = -F12
        F23 = m3 * a
        F32 = -F23

        # Dibujar los cuadrados representando las masas
        rec1 = Rectangle((0, 0), 1, 1, fill=True, edgecolor='black', facecolor='orange')
        rec2 = Rectangle((1, 0), 1, 1, fill=True, edgecolor='black', facecolor='white')
        rec3 = Rectangle((2, 0), 1, 1, fill=True, edgecolor='black', facecolor='turquoise')

        self.ax.add_patch(rec1)
        self.ax.add_patch(rec2)
        self.ax.add_patch(rec3)

        # Etiquetar las masas
        plt.text(0.5, 0.5, f'm1 = {m1}kg', color='black', weight='bold', ha='center', va='center', fontsize=12)
        plt.text(1.5, 0.5, f'm2 = {m2}kg', color='black', weight='bold', ha='center', va='center', fontsize=12)
        plt.text(2.5, 0.5, f'm3 = {m3}kg', color='black', weight='bold', ha='center', va='center', fontsize=12)

        # Etiquetar la aceleración en la parte inferior en formato LaTeX
        plt.text(1.5, -0.1, r'$\vec{a} =' + str(a) + 'm/s² \hat{i}$', color='black', ha='center', va='center', fontsize=18)

        # Dibujar los vectores de fuerza
        plt.arrow(0.6, 0.6, 0.4, 0, head_width=0.05, head_length=0.1, fc='red', ec='red')
        plt.arrow(1.4, 0.4, -0.4, 0, head_width=0.05, head_length=0.1, fc='red', ec='red')
        plt.arrow(1.6, 0.6, 0.4, 0, head_width=0.05, head_length=0.1, fc='red', ec='red')
        plt.arrow(2.4, 0.4, -0.4, 0, head_width=0.05, head_length=0.1, fc='red', ec='red')

        # Etiquetar las fuerzas
        plt.text(0.85, 0.65, f'F12 = {F12} N', color='black', ha='center', va='center', fontsize=12)
        plt.text(1.15, 0.35, f'F21 = {F21} N', color='black', ha='center', va='center', fontsize=12)
        # Etiquetar las fuerzas
        plt.text(1.85, 0.65, f'F23 = {F23} N', color='black', ha='center', va='center', fontsize=12)
        plt.text(2.15, 0.35, f'F32 = {F32} N', color='black', ha='center', va='center', fontsize=12)

        # Configurar los límites de los ejes y mostrar el gráfico
        self.ax.set_xlim([0, 3])
        self.ax.set_ylim([0, 1])

        plt.axis('off')

#*************************** Clase de Tercera Ley (FIN) ***************************************************************************************************************#