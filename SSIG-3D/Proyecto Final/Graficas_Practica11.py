## Archivo para la esfera Conductora. Practica 11.

import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from mpl_toolkits import mplot3d
import numpy as np
from matplotlib import cm

#*************************** Clase de Esfera Conductora ********************************************************************************************************
class Esfera_Conductora(FigureCanvas):
    #------------------ Función Inicial ------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Simulación de muestra ------------------------------------------------------------------
    def graficar_esfera_muestra(self):    
        q = 1   # Valor de la carga
        d = 2   # distancia
        R = 1   # Radio de la esfera

        # Malla esférica
        phi, theta = np.mgrid[0:2 * np.pi:100j, 0:np.pi:50j]
        x = R * np.sin(theta) * np.cos(phi)
        y = R * np.sin(theta) * np.sin(phi)
        z = R * np.cos(theta)

        # Densidad de carga en función de theta
        def densidad_carga(theta, R, d, q):
            return -q * (d**2 - R**2) / (4 * np.pi * R * (R**2 + d**2 - 2 * R * d * np.cos(theta))**(3/2))

        # Calcular la densidad de carga en cada punto de la malla
        densidad_carga = densidad_carga(theta, R, d, q)

        # Coordenadas de la carga puntual
        carga_puntual_pos = np.array([0, 0, d])

        # Calcular la carga imagen y su posición
        q_imagen = -q * (R / d)
        pos_imagen = (R**2 / d) * carga_puntual_pos / np.linalg.norm(carga_puntual_pos)

        # Crear el objeto mapeable de escalares con los límites correctos
        sm = cm.ScalarMappable(cmap=cm.jet, norm=plt.Normalize(vmin=densidad_carga.min(), vmax=densidad_carga.max()))
        sm.set_array([])

        # Graficar la esfera con la densidad de carga en colores
        surf = self.ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=sm.to_rgba(densidad_carga), linewidth=0, antialiased=False, alpha=0.5)

        # Dibujar la carga externa y la carga imagen
        self.ax.scatter(*carga_puntual_pos, c='red', marker='o', s=100, label='Carga externa')
        self.ax.scatter(*pos_imagen, c='blue', marker='o', s=100, label='Carga imagen')

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        # Desactivar los ejes y la cuadrícula
        self.ax.set_axis_off()
        self.ax.grid(False)

        # Ajustes del gráfico
        #self.ax.set_title('Densidad de carga en la superficie de una esfera conductora  [C/m**2]')
        plt.suptitle('Densidad de carga en la superficie de una esfera conductora  [C/m**2]')
        self.ax.set_title(r'$\sigma(\theta) = \frac{-q(d^2 - R^2)}{4 \pi R (R^2 + d^2 - 2Rd \cos(\theta))^{3/2}}$', fontsize=14, pad=20, loc='center')
        #self.ax.set_xlabel('Posición_X')
        #self.ax.set_ylabel('Posición_Y')
        #self.ax.set_zlabel('Posición_Z')
        self.ax.legend()

        # Establecer los límites de los ejes
        self.ax.set_xlim(-R, d)
        self.ax.set_ylim(-R, d)
        self.ax.set_zlim(-R, d)

        # Barra de colores
        cbar = self.fig.colorbar(sm, ax=self.ax, shrink=0.7, aspect=5)
        cbar.set_label('Densidad de carga C/m**2')
        plt.tight_layout()
    #------------ Simulación de muestra (FIN) ----------------------------------------

    #------------ Simulación de muestra ------------------------------------------------------------------
    def graficar_esfera(self, q, d):    
        R = 1

        # Malla esférica
        phi, theta = np.mgrid[0:2 * np.pi:100j, 0:np.pi:50j]
        x = R * np.sin(theta) * np.cos(phi)
        y = R * np.sin(theta) * np.sin(phi)
        z = R * np.cos(theta)

        # Densidad de carga en función de theta
        def densidad_carga(theta, R, d, q):
            return -q * (d**2 - R**2) / (4 * np.pi * R * (R**2 + d**2 - 2 * R * d * np.cos(theta))**(3/2))

        # Calcular la densidad de carga en cada punto de la malla
        densidad_carga = densidad_carga(theta, R, d, q)

        # Coordenadas de la carga puntual
        carga_puntual_pos = np.array([0, 0, d])

        # Calcular la carga imagen y su posición
        q_imagen = -q * (R / d)
        pos_imagen = (R**2 / d) * carga_puntual_pos / np.linalg.norm(carga_puntual_pos)

        # Crear el objeto mapeable de escalares con los límites correctos
        sm = cm.ScalarMappable(cmap=cm.jet, norm=plt.Normalize(vmin=densidad_carga.min(), vmax=densidad_carga.max()))
        sm.set_array([])

        # Graficar la esfera con la densidad de carga en colores
        surf = self.ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=sm.to_rgba(densidad_carga), linewidth=0, antialiased=False, alpha=0.5)

        # Dibujar la carga externa y la carga imagen
        if (q > 0):
            self.ax.scatter(*carga_puntual_pos, c='red', marker='o', s=100, label='Carga externa')
            self.ax.scatter(*pos_imagen, c='blue', marker='o', s=100, label='Carga imagen')
        else:
            self.ax.scatter(*carga_puntual_pos, c='blue', marker='o', s=100, label='Carga externa')
            self.ax.scatter(*pos_imagen, c='red', marker='o', s=100, label='Carga imagen')

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        # Desactivar los ejes y la cuadrícula
        self.ax.set_axis_off()
        self.ax.grid(False)

        # Ajustes del gráfico
        #self.ax.set_title('Densidad de carga en la superficie de una esfera conductora  [C/m**2]')
        plt.suptitle('Densidad de carga en la superficie de una esfera conductora  [C/m**2]')
        self.ax.set_title(r'$\sigma(\theta) = \frac{-q(d^2 - R^2)}{4 \pi R (R^2 + d^2 - 2Rd \cos(\theta))^{3/2}}$', fontsize=14, pad=20, loc='center')
        #self.ax.set_xlabel('Posición_X')
        #self.ax.set_ylabel('Posición_Y')
        #self.ax.set_zlabel('Posición_Z')
        self.ax.legend()

        # Establecer los límites de los ejes
        self.ax.set_xlim(-R, d)
        self.ax.set_ylim(-R, d)
        self.ax.set_zlim(-R, d)

        # Barra de colores
        cbar = self.fig.colorbar(sm, ax=self.ax, shrink=0.7, aspect=5)
        cbar.set_label('Densidad de carga C/m**2')
        plt.tight_layout()
    #------------ Simulación de muestra (FIN) ----------------------------------------

    #------------ Función para borrar la gráfica -----------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        #plt.clf()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------
    def cerrarGraf(self):
	    plt.close(self.fig)

