## Archivo para el módulo de "Ángulo Sólido"

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d
import numpy as np
import sympy as sp

#*************************** Clase de Ángulo Sólido *******************************************************************************************************************#
class Angulo_Solido(FigureCanvas):
    #------------------ Función Inicial---------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Ang. Solido -------------------------------------------------------------------------------------------------------------------------------
    def graficar_ang_solido(self, theta_cone, usuario):    
        self.ax.set_title("Hecho por: " + usuario, loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Ejemplo de ángulo sólido")  
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        # Parámetros de la esfera y el cono
        radius = 1
        #theta_cone = np.pi/6   # Ángulo theta respecto al eje Z (30 grados en este caso)
        solid_angle = 2 * np.pi * (1 - np.cos(theta_cone))

        # Convertir el resultado en múltiplos de π
        solid_angle_pi = solid_angle / np.pi

        # Simplificar la fracción y mostrar el resultado en múltiplos de π
        fraction = sp.Rational(solid_angle_pi).limit_denominator(100)
        #print("Ángulo sólido subtendido por el cono:", fraction, "π estereorradianes")
        subt1 = "Ángulo sólido subtendido por el cono: " +  str(fraction) + " π estereorradianes"
        self.ax.text2D(0.05, 0.92, subt1, transform=self.ax.transAxes)

        ##########################################################################################

        # Coordenadas esféricas
        phi = np.linspace(0, 2 * np.pi, 100)
        theta = np.linspace(0, np.pi, 100)
        phi, theta = np.meshgrid(phi, theta)

        # Coordenadas cartesianas de la esfera
        x = radius * np.sin(theta) * np.cos(phi)
        y = radius * np.sin(theta) * np.sin(phi)
        z = radius * np.cos(theta)

        # Coordenadas cilíndricas para el cono
        r_cone = np.linspace(0, radius, 100)
        cone_phi = np.linspace(0, 2 * np.pi, 100)
        r_cone, cone_phi = np.meshgrid(r_cone, cone_phi)

        # Coordenadas cartesianas del cono
        cone_x = r_cone * np.sin(theta_cone) * np.cos(cone_phi)
        cone_y = r_cone * np.sin(theta_cone) * np.sin(cone_phi)
        cone_z = r_cone * np.cos(theta_cone)

        # Dibujar la esfera con un color azul suave y cierta transparencia
        self.ax.plot_surface(x, y, z, color='lightskyblue', alpha=0.6, rstride=1, cstride=1)

        # Dibujar el cono con color gris y cierta transparencia
        self.ax.plot_surface(cone_x, cone_y, cone_z, color='gray', alpha=0.3, rstride=1, cstride=1)

        # Máscara para el área intersectada por el cono
        mask = theta <= theta_cone

        # Coordenadas cartesianas de la intersección
        x_intersect = x[mask]
        y_intersect = y[mask]
        z_intersect = z[mask]

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")
        self.ax.grid(False)
        self.ax.set_box_aspect([1, 1, 1])

        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_zticks([])

        # Dibujar la intersección en color rojo
        self.ax.scatter(x_intersect, y_intersect, z_intersect, color='red', s=1, alpha=1)

        plt.tight_layout()

    #------------ Función para guardar la gráfica ----------------------------------------------------------------------------------------------------------------------
    def guardar_graf(self, direccion):
        plt.savefig(direccion + "/AngSolido.jpg")
    #------------ Función para borrar la gráfica -----------------------------------------------------------------------------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()

#*************************** Clase de Ángulo Sólido (FIN) *************************************************************************************************************#