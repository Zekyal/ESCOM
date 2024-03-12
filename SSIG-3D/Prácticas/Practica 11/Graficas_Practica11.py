## Archivo para el módulo de Cosenos Directores
from PyQt5 import QtWidgets

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
        q = 1
        d = 2
        R = 1

        # Coordenadas de la carga puntual
        carga_puntual_pos = np.array([0, 0, d])

        # Calcular la carga imagen y su posición
        q_imagen = -q * (R / (d - R))
        pos_imagen = (R**2 / d) * carga_puntual_pos / np.linalg.norm(carga_puntual_pos)

        # Crear una malla esférica
        theta, phi = np.mgrid[0:2 * np.pi:100j, 0:np.pi:50j]
        x = R * np.sin(phi) * np.cos(theta)
        y = R * np.sin(phi) * np.sin(theta)
        z = R * np.cos(phi)

        # Calcular la densidad de carga en cada punto de la malla
        densidad_carga = np.zeros_like(phi)

        for i in range(theta.shape[0]):
            for j in range(theta.shape[1]):
                posicion_esfera = np.array([x[i, j], y[i, j], z[i, j]])
                distancia = np.linalg.norm(pos_imagen - posicion_esfera)
                densidad_carga[i, j] = q_imagen / distancia**2

        # Normalizar la densidad de carga para la visualización
        densidad_carga_norm = (densidad_carga - densidad_carga.min()) / (densidad_carga.max() - densidad_carga.min())

        # Igualar la relación de aspecto de los ejes
        self.ax.set_box_aspect([1, 1, 1])

        # Desactivar los ejes y la cuadrícula
        self.ax.set_axis_off()
        self.ax.grid(False)

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        # Graficar la esfera con la densidad de carga
        self.ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=cm.jet(densidad_carga_norm), linewidth=0, alpha=0.5)

        # Agregar la carga puntual y la carga imagen
        self.ax.scatter(*carga_puntual_pos, c='red', marker='o', s=50, label='Carga puntual')
        self.ax.scatter(*pos_imagen, c='blue', marker='o', s=50, label='Carga imagen')

        # Configurar la gráfica
        self.ax.set_title("Distribución de carga eléctrica en una esfera conductora, debido a una carga puntual", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.legend()
        # Establecer los límites de los ejes
        self.ax.set_xlim(-R, d)
        self.ax.set_ylim(-R, d)
        self.ax.set_zlim(-R, d)

        # Crear la barra de colores
        mappable = cm.ScalarMappable(cmap=cm.jet)
        mappable.set_array(densidad_carga)
        plt.colorbar(mappable, ax=self.ax, label="Densidad de carga")
        plt.tight_layout()
    #------------ Simulación de muestra (FIN) ----------------------------------------

    #------------ Simulación de muestra ------------------------------------------------------------------
    def graficar_esfera(self, q, d):    
        R = 1

        # Coordenadas de la carga puntual
        carga_puntual_pos = np.array([0, 0, d])

        # Calcular la carga imagen y su posición
        q_imagen = -q * (R / (d - R))
        pos_imagen = (R**2 / d) * carga_puntual_pos / np.linalg.norm(carga_puntual_pos)

        # Crear una malla esférica
        theta, phi = np.mgrid[0:2 * np.pi:100j, 0:np.pi:50j]
        x = R * np.sin(phi) * np.cos(theta)
        y = R * np.sin(phi) * np.sin(theta)
        z = R * np.cos(phi)

        # Calcular la densidad de carga en cada punto de la malla
        densidad_carga = np.zeros_like(phi)

        for i in range(theta.shape[0]):
            for j in range(theta.shape[1]):
                posicion_esfera = np.array([x[i, j], y[i, j], z[i, j]])
                distancia = np.linalg.norm(pos_imagen - posicion_esfera)
                densidad_carga[i, j] = q_imagen / distancia**2

        # Normalizar la densidad de carga para la visualización
        densidad_carga_norm = (densidad_carga - densidad_carga.min()) / (densidad_carga.max() - densidad_carga.min())

        # Igualar la relación de aspecto de los ejes
        self.ax.set_box_aspect([1, 1, 1])

        # Desactivar los ejes y la cuadrícula
        self.ax.set_axis_off()
        self.ax.grid(False)

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        # Graficar la esfera con la densidad de carga
        self.ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=cm.jet(densidad_carga_norm), linewidth=0, alpha=0.5)

        # Agregar la carga puntual y la carga imagen
        if (q > 0):
            self.ax.scatter(*carga_puntual_pos, c='red', marker='o', s=50, label='Carga puntual')
            self.ax.scatter(*pos_imagen, c='blue', marker='o', s=50, label='Carga imagen')
        else:
            self.ax.scatter(*carga_puntual_pos, c='blue', marker='o', s=50, label='Carga puntual')
            self.ax.scatter(*pos_imagen, c='red', marker='o', s=50, label='Carga imagen')

        # Configurar la gráfica
        self.ax.set_title("Distribución de carga eléctrica en una esfera conductora, debido a una carga puntual", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        #self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        #self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        #self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.legend()
        # Establecer los límites de los ejes
        self.ax.set_xlim(-R, d)
        self.ax.set_ylim(-R, d)
        self.ax.set_zlim(-R, d)

        # Crear la barra de colores
        mappable = cm.ScalarMappable(cmap=cm.jet)
        mappable.set_array(densidad_carga)
        plt.colorbar(mappable, ax=self.ax, label="Densidad de carga")
        plt.tight_layout()
    #------------ Simulación de muestra (FIN) ----------------------------------------

    #------------ Función para borrar la gráfica -----------------------------------------------------
    def vaciar_grafica(self):
        self.ax.cla()
        #plt.clf()

    #------------ Función para borrar la gráfica (FIN) -----------------------------------------------
