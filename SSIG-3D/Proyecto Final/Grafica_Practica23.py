# Archivo con el proceso de graficación y animación. Practica 23

from PyQt5 import QtWidgets
import matplotlib.pyplot as plt ## Creación de gráficas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # Juntar matplotlib con las interfaces de Qt Designer
from matplotlib.animation import FuncAnimation #Animaciones de las gráficas
from mpl_toolkits import mplot3d
import numpy as np

#*************************** Clase de Segunda Ley *********************************************************************************************************************#
class Inercial(FigureCanvas):
    #------------------ Función Inicial---------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, figure=None):

        self.fig = plt.figure()
        self.ax = plt.axes(projection="3d")
        super().__init__(self.fig)

    #------------ Grafica de Sistema Inercial --------------------------------------------------------------------------------------------------------------------
    def graficar_inercial(self):    
        self.ax.set_title("Hecho por: SSIG-3D", loc = "center", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})    # Título de la Gráfica
        plt.suptitle("Sistema de Referencia Inercial y No Inercial")  
        self.ax.set_xlabel("Posición_X", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})   # Inserta el nombre al eje X
        self.ax.set_ylabel("Posición_Y", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        self.ax.set_zlabel("Posición_Z", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})

        global rotated_axes_lines, moving_origin_text
        rotated_axes_lines = []

        # Color de Fondo
        self.ax.set_facecolor("darkgrey")

        def rotate_x(points, angle):
            rotation_matrix = np.array([
                [1, 0, 0],
                [0, np.cos(angle), -np.sin(angle)],
                [0, np.sin(angle), np.cos(angle)],
            ])
            return np.dot(points, rotation_matrix)

        ##############################dEFINE ANIMATE##################################

        ############################################################################################################

        def animate(i):
            global x2_rotated, y2_rotated, z2_rotated, rotated_axes_lines, quivers
            displacement = i / 50.0
            translation_vector = np.array([0,1.0*displacement*np.cos(angle), -1.0*displacement*np.sin(angle)])
            rotated_points_translated = np.add(rotated_points, translation_vector)
            x2_rotated, y2_rotated, z2_rotated = rotated_points_translated.T
            
            origin = np.array([translation_vector[0], translation_vector[1], translation_vector[2]])
            
            for line in rotated_axes_lines:
                line.remove()
            rotated_axes_translated = np.add(rotated_axes, translation_vector)
            rotated_axes_lines = []
            for i in range(3):
                line = self.ax.plot([translation_vector[0], rotated_axes_translated[i, 0]], [translation_vector[1], rotated_axes_translated[i, 1]], [translation_vector[2], rotated_axes_translated[i, 2]], color=colors[i])
                rotated_axes_lines.append(line[0])

            if 'quivers' in globals():
                for q in quivers:
                    q.remove()
            quivers = []
            for x, y, z in zip(x2_rotated, y2_rotated, z2_rotated):
                u = x - origin[0]
                v = y - origin[1]
                w = z - origin[2]
                q = self.ax.quiver(origin[0], origin[1], origin[2], u, v, w, color='red')
                quivers.append(q)

        # Move the "O'" text with the moving coordinate system
            global moving_origin_text
            moving_origin_text = self.ax.text(origin[0], origin[1], origin[2], "O'", color='red')
            if moving_origin_text:
                moving_origin_text.remove()
            
            # Update the acceleration value in the subtitle
            acx = 1.0  # Calculate the acceleration value here
            acx_text.set_text(f"acx = {acx:.2f}  [m/s²]")

            return quivers,
        
        ############ TERMINA ANIMATE#######################################################

        ##########################

        # Define the fixed vector
        fixed_vector = np.array([0.5, 0.5, 0.5])

        x1, y1, z1 = fixed_vector

        x2 = x1
        y2 = y1
        z2 = z1
        dalpha = -30
        angle = np.radians(dalpha)
        points = np.vstack((x2, y2, z2)).T
        rotated_points = rotate_x(points, angle)
        x2_rotated, y2_rotated, z2_rotated = rotated_points.T

        #scatter = ax.scatter(x2_rotated, y2_rotated, z2_rotated, color='red')
        #quiver = ax.quiver(x2_rotated[:-1], y2_rotated[:-1], z2_rotated[:-1], x2_rotated[1:]-x2_rotated[:-1], y2_rotated[1:]-y2_rotated[:-1], z2_rotated[1:]-z2_rotated[:-1], color='red')

        self.ax.plot([0, 1], [0, 0], [0, 0], color='black')
        self.ax.plot([0, 0], [0, 1], [0, 0], color='black')
        self.ax.plot([0, 0], [0, 0], [0, 1], color ='black')

        rotated_axes = rotate_x(np.eye(3), angle)
        colors = ['red', 'green', 'blue']
        rotated_axes_lines = []
        for i in range(3):
            line = self.ax.plot([0, rotated_axes[i, 0]], [0, rotated_axes[i, 1]], [0, rotated_axes[i, 2]], color=colors[i])
            rotated_axes_lines.append(line[0])

        ####Crea el
        for i in np.linspace(-1, 1, 5):
            self.ax.plot([-1, 1], [i, i], [0, 0], color='gray', alpha=0.3)
            self.ax.plot([i, i], [-1, 1], [0, 0], color='gray', alpha=0.3)

        #######################

        xy_points = np.array([[i, j, 0] for i in np.linspace(-1, 1, 5) for j in np.linspace(-1, 1, 5)])
        rotated_xy_points = rotate_x(xy_points, angle)
        for i in range(0, len(rotated_xy_points), 5):
            self.ax.plot(rotated_xy_points[i:i+5, 0], rotated_xy_points[i:i+5, 1], rotated_xy_points[i:i+5, 2], color='red', alpha=0.3)
        for i in range(5):
            self.ax.plot(rotated_xy_points[i::5, 0], rotated_xy_points[i::5, 1], rotated_xy_points[i::5, 2], color='red', alpha=0.3)

        self.ax.plot([0, 0], [0, 1], [0, 0], color='green')

        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.ax.set_zlim(-1, 1)

        self.ani = FuncAnimation(self.fig, animate, frames=50, interval=50)

        fixed_origin_text = self.ax.text(0, 0, 0, 'O', color='blue')
        moving_origin_text = None

        plt.figtext(0.15, 0.70, "O = sistema de referencia inercial", fontsize=12, color='blue')
        plt.figtext(0.15, 0.65, "O' = sistema de referencia no inercial", fontsize=12, color='red')
        acx_text = plt.figtext(0.15, 0.60, "", fontsize=12, color='black')
        plt.tight_layout()
    #------------ Grafica de Segunda Ley de muestra (FIN) --------------------------------------------------------------------------------------------------------------
    def cerrarGraf(self):
	    plt.close(self.fig)
#*************************** Clase de Segunda Ley (FIN) ***************************************************************************************************************#