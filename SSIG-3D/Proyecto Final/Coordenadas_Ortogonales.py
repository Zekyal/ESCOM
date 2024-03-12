## Archivo para el módulo de Coordenadas Ortogonales

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d
import numpy as np

#*************************** Clase de Coordenadas Cartesianas *********************************************************************************************************#
class Coordenadas_Cartesianas(FigureCanvas):
    #------------------ Función Inicial---------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Coor. Cartesianas -------------------------------------------------------------------------------------------------------------------------
    def graficar_coor_carte(self, x_v, y_v, z_v, usuario):    
        self.ax.set_title("Hecho por: " + usuario, loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Ejemplo de coordenadas cartesianas")   
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        magnitud = np.sqrt(pow(x_v, 2) + pow(y_v, 2) + pow(z_v, 2))
        self.ax.text(1.25*x_v, 1.25*y_v, 1.25*z_v, "r = |v| = " + str(round(magnitud, 2)), color='black', style='italic', fontweight='bold', fontsize=12)

        # Coordenada 'theta'
        if(z_v > 0):     # z > 0
            theta = np.arctan(np.sqrt(pow(x_v, 2) + pow(y_v, 2))/z_v)
        elif(z_v < 0):   # z < 0
            theta = np.pi + np.arctan(np.sqrt(pow(x_v, 2) + pow(y_v, 2))/z_v)
        else:           # z = 0
            if(x_v == 0 and y_v == 0):    # z = x = y = 0
                theta = 0
            else:                       # z = 0 and xy =! 0                   
                theta = np.pi/2

        # Coordenada 'phi'
        if(x_v > 0 ):    # x > 0
            phi = np.arctan(y_v/x_v)
        elif(x_v < 0):   # x < 0
            if(y_v >= 0):    # x < 0 and y >= 0 
                phi = np.arctan(y_v/x_v) + np.pi
            elif(y_v < 0):   # x < 0 and y < 0
                phi = np.arctan(y_v/x_v) - np.pi
        else:           # x = 0 
            if(y_v > 0):     # x = 0 and y > 0
                phi = np.pi/2
            elif(y_v < 0):   # x = 0 and y < 0
                phi = -np.pi/2
            else:           # x = 0 and y = 0
                phi = 0

        # Definicion de los ejes x, y, z que se marcaran para definir la grafica
        if (x_v >= 0 ):
            self.ax.plot((0, 1.25*x_v), (0, 0), (0, 0), color = "orange", label='X')
            self.ax.text(1.25*x_v, 0, 0, 'X', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((1.25*x_v, 0), (0, 0), (0, 0), color = "red", label='-X')
            self.ax.text(1.25*x_v, 0, 0, '-X', color='teal', style='italic', fontweight='bold', fontsize=12)
        
        if (y_v >= 0 ):
            self.ax.plot((0, 0), (0, 1.25*y_v), (0, 0), color = "green", label='Y')
            self.ax.text(0, 1.25*y_v, 0, 'Y', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (1.25*y_v, 0), (0, 0), color = "blue", label='-Y')
            self.ax.text(0, 1.25*y_v, 0, '-Y', color='teal', style='italic', fontweight='bold', fontsize=12)

        if (z_v >= 0):
            self.ax.plot((0, 0), (0, 0), (0, 1.25*z_v), color = "slateblue", label='Z')
            self.ax.text(0, 0, 1.25*z_v, 'Z', color='teal', style='italic', fontweight='bold', fontsize=12)
        else:
            self.ax.plot((0, 0), (0, 0), (1.25*z_v, 0), color = "brown", label='-Z')
            self.ax.text(0, 0, 1.25*z_v, '-Z', color='teal', style='italic', fontweight='bold', fontsize=12)

        self.ax.plot((x_v, x_v), (0, y_v), (0, 0), color = "black", linestyle = "dotted")
        self.ax.plot((0, x_v), (y_v, y_v), (0, 0), color = "black", linestyle = "dotted")
        self.ax.plot((x_v, x_v), (y_v, y_v), (0, z_v), color = "black", linestyle = "dotted")
        self.ax.plot((0, x_v), (0, x_v*np.tan(phi)), (0, 0), color = "black", linestyle = "dotted")
        self.ax.plot((0, x_v), (0, x_v*np.tan(phi)), (z_v, z_v), color = "black", linestyle = "dotted")

        # ----------    Curvas de los angulos   ----------
        sgnRx = x_v/np.absolute(x_v)
        sgnRy = y_v/np.absolute(y_v)
        sgnzRz = z_v/np.absolute(z_v)

        # ->    Curva con respecto al eje z (ángulo θ)
        # generacion de todos los valores de z
        z = np.linspace(0, (0.5 * x_v * z_v)/np.sqrt(pow(x_v, 2) + pow(y_v, 2) + pow(z_v, 2)), 1000) 

        # formulas
        X = np.absolute(z) * sgnRx
        Y = np.absolute((y_v / x_v) * z) * sgnRy
        Z = sgnzRz * np.sqrt((pow(z_v, 2)/4) - pow(z, 2) * ((pow(x_v, 2) + pow(y_v, 2))/pow(x_v, 2)))
        self.ax.plot(X, Y, Z, color = "mediumvioletred", label = 'θ')
        self.ax.text(X[500], Y[500], Z[500], 'θ = ' + str(round(np.absolute(np.rad2deg(theta)), 2)) + '°', style='italic', fontweight='bold', color = "mediumvioletred", fontsize=12)

        # ->    Curva con respecto al eje x (ángulo φ)
        # generacion de todos los valores de x
        x = np.linspace(0, (0.5 * y_v * x_v)/np.sqrt(pow(x_v, 2) + pow(y_v, 2) + pow(z_v, 2)), 1000) 

        # formulas
        X = sgnRx * np.sqrt((pow(x_v, 2)/4) - pow(x, 2) * ((pow(y_v, 2) + pow(z_v, 2))/pow(y_v, 2)))
        Y = np.absolute(x) * sgnRy
        Z = 0
        self.ax.plot(X, Y, Z, color = "red", label = 'φ')
        self.ax.text(X[500], Y[500], 0, 'φ = ' + str(round(np.absolute(np.rad2deg(phi)), 2)) + '°', style='italic', fontweight='bold', color = "red", fontsize=12)

        self.ax.quiver(0, 0, 0, x_v, y_v, z_v, arrow_length_ratio=0.1)
        self.ax.text(x_v, y_v, z_v, "(" + str(round(x_v, 2)) + ", " + str(round(y_v, 2)) + ", " + str(round(z_v, 2)) + ")", style='italic', fontweight='bold', color = plt.rcParams['axes.prop_cycle'].by_key()['color'][0], fontsize=12)
        self.ax.text(3*x_v/4, 3*y_v/4, 3*z_v/4, 'r', style='italic', fontweight='bold', color = plt.rcParams['axes.prop_cycle'].by_key()['color'][0], fontsize=12)
        plt.legend(loc = 8, ncols = 3, draggable = True) # Muestra las etiquetas

        plt.tight_layout()

    #------------ Función para guardar la gráfica ----------------------------------------------------------------------------------------------------------------------
    def guardar_graf(self, direccion):
        plt.savefig(direccion + "/CoorCartesianas.jpg")
    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

#*************************** Clase de Coordenadas Cartesianas (FIN) ***************************************************************************************************#

#*************************** Clase de Coordenadas Esféricas ***********************************************************************************************************#
class Coordenadas_Esfericas(FigureCanvas):
    #------------------ Función Inicial---------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Coor. Esféricas ---------------------------------------------------------------------------------------------------------------------------
    def graficar_coor_esfe(self, x_v, y_v, z_v, usuario):    
        self.ax.set_title("Hecho por: " + usuario, loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        def draw_sphere(radius, theta, phi, v_r,v_t,v_p): 
            
            # Parámetros de la esfera
            u = np.linspace(0, 2 * np.pi, 100)
            v = np.linspace(0, np.pi, 100)
            x = radius * np.outer(np.cos(u), np.sin(v))
            y = radius * np.outer(np.sin(u), np.sin(v))
            z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

            # Dibujar esfera
            self.ax.plot_surface(x, y, z, color='orange', alpha=0.3)

            # Dibujar círculo rojo paralelo al plano XY
            phi_red = np.linspace(0, 2 * np.pi, 100)
            x_red = radius * np.sin(theta) * np.cos(phi_red)
            y_red = radius * np.sin(theta) * np.sin(phi_red)
            z_red = radius * np.cos(theta) * np.ones_like(phi_red)
            self.ax.plot(x_red, y_red, z_red, linestyle='dashed', color='red')

        # Dibujar El ecuador plano XY
            phi_red = np.linspace(0, 2 * np.pi, 100)
            x_red = radius * np.sin(pi/2) * np.cos(phi_red)
            y_red = radius * np.sin(pi/2) * np.sin(phi_red)
            z_red = radius * np.cos(pi/2) * np.ones_like(phi_red)
            self.ax.plot(x_red, y_red, z_red, linestyle='dashed', color='black')

            # Dibujar círculo azul perpendicular al plano XY
            theta_blue = np.linspace(0,2*np.pi, 100)
            x_blue = radius * np.sin(theta_blue) * np.cos(phi)
            y_blue = radius * np.sin(theta_blue) * np.sin(phi)
            z_blue = radius * np.cos(theta_blue)
            self.ax.plot(x_blue, y_blue, z_blue, linestyle='dashed', color='blue')

            # Dibujar ejes ortogonales
            self.ax.quiver(0, 0, 0, radius, 0, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
            self.ax.quiver(0, 0, 0, 0, radius, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
            self.ax.quiver(0, 0, 0, 0, 0, radius, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
            self.ax.quiver(0, 0, 0, -radius, 0, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
            self.ax.quiver(0, 0, 0, 0, -radius, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
            self.ax.quiver(0, 0, 0, 0, 0, -radius, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)

            # Agregar etiquetas a los ejes
            self.ax.text(radius, 0, 0, 'X', fontsize=12)
            self.ax.text(-radius, 0, 0, '-X', fontsize=12)
            self.ax.text(0, radius, 0, 'Y', fontsize=12)
            self.ax.text(0, -radius, 0, '-Y', fontsize=12)
            self.ax.text(0, 0, radius, 'Z', fontsize=12)
            self.ax.text(0, 0, -radius, '-Z', fontsize=12)

            plt.suptitle(f'Ejemplo de coordenadas esféricas: Esfera de radio {radius}')

        # Dibujar vector desde el origen al punto (r*sin(theta)*cos(phi), r*sin(theta)*sin(phi), r*cos(theta))
            vector_x = radius * np.sin(theta) * np.cos(phi)
            vector_y = radius * np.sin(theta) * np.sin(phi)
            vector_z = radius * np.cos(theta)
            self.ax.quiver(0, 0, 0, vector_x, vector_y, vector_z, color='green', linewidth=1.5, arrow_length_ratio=0.1)

        # Línea 1
            x1_start, y1_start, z1_start = 0, 0, 0
            x1_end, y1_end, z1_end = vector_x, vector_y, 0
            self.ax.plot([x1_start, x1_end], [y1_start, y1_end], [z1_start, z1_end], linestyle='dotted', color='black')

        # Línea 2
            x2_start, y2_start, z2_start = x1_end, y1_end, z1_end
            x2_end, y2_end, z2_end = vector_x, vector_y, vector_z
            self.ax.plot([x2_start, x2_end], [y2_start, y2_end], [z2_start, z2_end], linestyle='dotted', color='black')

        # Línea 3
            x3_start, y3_start, z3_start = 0, 0, vector_z
            x3_end, y3_end, z3_end = vector_x, vector_y, vector_z
            self.ax.plot([x3_start, x3_end], [y3_start, y3_end], [z3_start, z3_end], linestyle='dotted', color='black')

        # Dibujar vector desde el origen al punto (r*sin(theta)*cos(phi), r*sin(theta)*sin(phi), r*cos(theta))
            vector_x = radius * np.sin(theta) * np.cos(phi)
            vector_y = radius * np.sin(theta) * np.sin(phi)
            vector_z = radius * np.cos(theta)
            self.ax.quiver(0, 0, 0, vector_x, vector_y, vector_z, color='green', linewidth=1.5, arrow_length_ratio=0.1)

        # Dibujar vectores unitarios v_r, v_t y v_p y agregar etiquetas de texto
            self.ax.quiver(vector_x, vector_y, vector_z, v_r[0], v_r[1], v_r[2], color='green', linewidth=1.5, arrow_length_ratio=0.1)
            self.ax.text(vector_x + v_r[0], vector_y + v_r[1], vector_z + v_r[2], r'$\hat{r}$', fontsize=10)

            self.ax.quiver(vector_x, vector_y, vector_z, v_t[0], v_t[1], v_t[2], color='blue', linewidth=1.5, arrow_length_ratio=0.1)
            self.ax.text(vector_x + v_t[0], vector_y + v_t[1], vector_z + v_t[2], r'$\hat{\theta}$', fontsize=10)

            self.ax.quiver(vector_x, vector_y, vector_z, v_p[0], v_p[1], v_p[2], color='red', linewidth=1.5, arrow_length_ratio=0.1)
            self.ax.text(vector_x + v_p[0], vector_y + v_p[1], vector_z + v_p[2], r'$\hat{\phi}$', fontsize=10)

        # Agregar título y subtítulos
            subt1 = r'$\hat{{\theta}} = ({:.3f}, {:.3f}, {:.3f})$'.format(v_t[0], v_t[1], v_t[2])
            subt2 = r'$\hat{{\phi}} = ({:.3f}, {:.3f}, {:.3f})$'.format(v_p[0], v_p[1], v_p[2])
            self.ax.text2D(0.05, 0.92, subt1, transform=self.ax.transAxes)
            self.ax.text2D(0.05, 0.88, subt2, transform=self.ax.transAxes)

        # Ejemplo de uso
        pi = np.pi
        v_x = np.array([1,0,0])
        v_y = np.array([0,1,0])
        v_z = np.array([0,0,1])

        radio = np.sqrt(pow(x_v,2) + pow(y_v,2) +pow(z_v,2))

        # Calcula ángulo theta y ángulo phi
        if x_v == 0 and y_v > 0:
            angulo_phi = 0.5 * pi
        elif x_v == 0 and y_v < 0:
            angulo_phi = 1.5 * pi
        elif y_v == 0 and x_v > 0:
            angulo_phi = 0
        elif y_v == 0 and x_v < 0:
            angulo_phi = pi
        elif x_v == 0 and y_v == 0:
            angulo_theta = 0
            angulo_phi = 0    
        else:
            angulo_phi = np.arctan2(y_v, x_v)

        angulo_theta = np.arccos(z_v / radio)
        #print('angulo_theta, angulo_phi =  ', angulo_theta, angulo_phi)

        v_r = np.sin(angulo_theta)*np.cos(angulo_phi)*v_x + np.sin(angulo_theta)*np.sin(angulo_phi)*v_y + np.cos(angulo_theta)*v_z
        v_t = np.cos(angulo_theta)*np.cos(angulo_phi)*v_x + np.cos(angulo_theta)*np.sin(angulo_phi)*v_y - np.sin(angulo_theta)*v_z
        v_p = -np.sin(angulo_phi)*v_x + np.cos(angulo_phi)*v_y

        draw_sphere(radio, angulo_theta, angulo_phi,v_r,v_t,v_p)

        # ----------    Curvas de los angulos   ----------
        sgnRx = x_v/np.absolute(x_v)
        sgnRy = y_v/np.absolute(y_v)
        sgnzRz = z_v/np.absolute(z_v)

        # ->    Curva con respecto al eje z (ángulo θ)
        # generacion de todos los valores de z
        z = np.linspace(0, (0.5 * x_v * z_v)/np.sqrt(pow(x_v, 2) + pow(y_v, 2) + pow(z_v, 2)), 1000) 

        # formulas
        X = np.absolute(z) * sgnRx
        Y = np.absolute((y_v / x_v) * z) * sgnRy
        Z = sgnzRz * np.sqrt((pow(z_v, 2)/4) - pow(z, 2) * ((pow(x_v, 2) + pow(y_v, 2))/pow(x_v, 2)))
        self.ax.plot(X, Y, Z, color = "black", label = 'θ')
        self.ax.text(X[500], Y[500], Z[500], 'θ = ' + str(round(np.absolute(np.rad2deg(angulo_theta)), 2)) + '°', style='italic', fontweight='bold', color = "black", fontsize=12)

        # ->    Curva con respecto al eje x (ángulo φ)
        # generacion de todos los valores de x
        x = np.linspace(0, (0.5 * y_v * x_v)/np.sqrt(pow(x_v, 2) + pow(y_v, 2) + pow(z_v, 2)), 1000) 

        # formulas
        X = sgnRx * np.sqrt((pow(x_v, 2)/4) - pow(x, 2) * ((pow(y_v, 2) + pow(z_v, 2))/pow(y_v, 2)))
        Y = np.absolute(x) * sgnRy
        Z = 0
        self.ax.plot(X, Y, Z, color = "black", label = 'φ')
        self.ax.text(X[500], Y[500], 0, 'φ = ' + str(round(np.absolute(np.rad2deg(angulo_phi)), 2)) + '°', style='italic', fontweight='bold', color = "black", fontsize=12)

        self.ax.quiver(0, 0, 0, x_v, y_v, z_v, arrow_length_ratio=0.1)
        self.ax.text(3*x_v/4, 3*y_v/4, 3*z_v/4, 'r', style='italic', fontweight='bold', color = plt.rcParams['axes.prop_cycle'].by_key()['color'][0], fontsize=12)

        plt.tight_layout()

    #------------ Función para guardar la gráfica ----------------------------------------------------------------------------------------------------------------------
    def guardar_graf(self, direccion):
        plt.savefig(direccion + "/CoorEsfericas.jpg")
    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

#*************************** Clase de Coordenadas Esféricas (FIN) *****************************************************************************************************#

#*************************** Clase de Coordenadas Cilíndricas *********************************************************************************************************#
class Coordenadas_Cilindricas(FigureCanvas):
    #------------------ Función Inicial---------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Coor. Esféricas ---------------------------------------------------------------------------------------------------------------------------
    def graficar_coor_cilin(self, x, y, z, usuario):    
        self.ax.set_title("Hecho por: " + usuario, loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Ejemplo de coordenadas cilíndricas")  
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        # Convertir a coordenadas cilíndricas
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan2(y, x)
        h = z

        # Crear malla de coordenadas cilíndricas
        theta_vals = np.linspace(0, 2*np.pi, 50)
        z_vals = np.linspace(0, h, 50)
        theta_vals, z_vals = np.meshgrid(theta_vals, z_vals)
        r_vals = np.ones_like(theta_vals) * r
        x_vals = r_vals * np.cos(theta_vals)
        y_vals = r_vals * np.sin(theta_vals)

        # Dibujar cilindro
        self.ax.plot_surface(x_vals, y_vals, z_vals, alpha = 0.5, color= 'tomato')

        # Dibujar ejes ortogonales
        self.ax.quiver(0, 0, 0, r, 0, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
        self.ax.quiver(0, 0, 0, 0, r, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
        self.ax.quiver(0, 0, 0, -r, 0, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
        self.ax.quiver(0, 0, 0, 0, -r, 0, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)
        self.ax.quiver(0, 0, 0, 0, 0, z, color='black', linestyle='-', linewidth=1, arrow_length_ratio=0.1)

        # Agregar etiquetas a los ejes
        self.ax.text(r, 0, 0, 'X', fontsize=12)
        self.ax.text(0, r, 0, 'Y', fontsize=12)
        self.ax.text(-r, 0, 0, '-X', fontsize=12)
        self.ax.text(0, -r, 0, '-Y', fontsize=12)
        self.ax.text(0, 0, h, 'Z', fontsize=12)

        self.ax.quiver(0, 0, 0, x, y, z, color='green', linewidth=1.5, arrow_length_ratio=0.1)

        # Línea 1
        x1_start, y1_start, z1_start = 0, 0, 0
        x1_end, y1_end, z1_end = x, y, 0
        self.ax.plot([x1_start, x1_end], [y1_start, y1_end], [z1_start, z1_end], linestyle='dotted', color='black')
        self.ax.text(x1_end/2, y1_end/2, z1_end, 'r', fontsize=12)

        # Línea 2
        x2_start, y2_start, z2_start = x1_end, y1_end, z1_end
        x2_end, y2_end, z2_end = x, y, z
        self.ax.plot([x2_start, x2_end], [y2_start, y2_end], [z2_start, z2_end], linestyle='dotted', color='black')
        self.ax.text(x2_end, y2_end, z2_end/2, 'h', fontsize=12)

        # Línea 3
        x3_start, y3_start, z3_start = 0, 0, z
        x3_end, y3_end, z3_end = x, y, z
        self.ax.plot([x3_start, x3_end], [y3_start, y3_end], [z3_start, z3_end], linestyle='dotted', color='black')

        # ----------    Curvas de los angulos   ----------

        # ->    Curva con respecto al eje x (ángulo θ)
        # generacion de todos los valores de x
        y_v = np.linspace(0, (0.5 * y * x)/np.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2)), 1000) 

        # formulas
        if (y != 0):
            X = np.sqrt((pow(x, 2)/4) - pow(y_v, 2) * ((pow(y, 2) + pow(z, 2))/pow(y, 2)))
        else:
            X = np.zeros((1000))
        Y = np.absolute(y_v)
        Z = 0
        self.ax.plot(X, Y, Z, color = "black", label = 'θ')
        self.ax.text(X[500], Y[500], 0, 'θ = ' + str(round(np.absolute(np.rad2deg(theta)), 2)) + '°', style='italic', fontweight='bold', color = "black", fontsize=12)
        
        plt.tight_layout()
        
    #------------ Función para guardar la gráfica ----------------------------------------------------------------------------------------------------------------------
    def guardar_graf(self, direccion):
        plt.savefig(direccion + "/CoorCilindricas.jpg")
    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

#*************************** Clase de Coordenadas Cilíndricas (FIN) ***************************************************************************************************#